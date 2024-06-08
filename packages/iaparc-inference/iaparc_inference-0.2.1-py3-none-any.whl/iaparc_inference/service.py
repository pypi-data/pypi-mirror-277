"""
IA Parc Inference service
Support for inference of IA Parc models
"""
import os
import io
import asyncio
import uuid
import threading
from inspect import signature
import logging
import logging.config
from typing import Tuple
import nats
from nats.errors import TimeoutError as NATSTimeoutError
from json_tricks import dumps, loads
from iaparc_inference.config import Config
from iaparc_inference.data_handler import DataHandler


LEVEL = os.environ.get('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(
    level=LEVEL,
    force=True,
    format="%(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
LOGGER = logging.getLogger("Inference")
LOGGER.propagate = True


class IAPListener():
    """
    Inference Listener class
    """

    def __init__(self,
                 callback,
                 batch: int = -1,
                 config_path: str = "/opt/pipeline/pipeline.json",
                 url: str = "",
                 queue: str = "",
                 ):
        """
        Constructor
        Arguments:
        - callback:     callback function to process data
                        callback(data: List[bytes], is_batch: bool) -> Tuple[List[bytes], str]
        Optional arguments:
        - batch:        batch size for inference (default: -1)
                        If your model do not support batched input, set batch to 1
                        If set to -1, batch size will be determined by the BATCH_SIZE 
                        environment variable
        - config_path:  path to config file (default: /opt/pipeline/pipeline.json)
        - url:          url of inference server (default: None)
                        By default determined by the NATS_URL environment variable,
                        however you can orverride it here
        - self.queue:        name of self.queue (default: None)
                        By default determined by the NATS_self.queue environment variable,
                        however you can orverride it here
        """
        self._lock = threading.Lock()
        self._subs_in = {}
        self._subs_out = []
        self.callback = callback
        sig = signature(callback)
        self.callback_args = sig.parameters
        nb_params = len(self.callback_args)
        if nb_params == 1:
            self.callback_has_parameters = False
        else:
            self.callback_has_parameters = True
        
        self.batch = batch
        self.config_path = config_path
        self.url = url
        self.queue = queue
        # Init internal variables
        self._dag = Config(self.config_path)
        self._inputs_name = self._dag.inputs.split(",")
        self._outputs_name = self._dag.outputs.split(",")
        self.inputs = {}
        for entity in self._dag.pipeline:
            for item in entity.input_def:
                if "name" in item and item["name"] in self._inputs_name:
                    self.inputs[item["name"]] = item

    @property
    def dag(self) -> Config:
        """ Input property """
        return self._dag

    @property
    def inputs_name(self) -> list:
        """ Input property """
        return self._inputs_name

    @property
    def outputs_name(self) -> list:
        return self._outputs_name

    def run(self):
        """
        Run inference service
        """
        if self.url == "":
            self.url = os.environ.get("NATS_URL", "nats://localhost:4222")
        if self.queue == "":
            self.queue = os.environ.get("NATS_QUEUE", "inference")
        if self.batch == -1:
            self.batch = int(os.environ.get("BATCH_SIZE", 1))
        self.queue = self.queue.replace("/", "-")
        asyncio.run(self._run_async())

    async def _run_async(self):
        """ Start listening to NATS messages
        url: NATS server url
        batch_size: batch size
        """
        nc = await nats.connect(self.url)
        js = nc.jetstream()
        
        for name in self.inputs_name:    
            queue_in = self.queue + "." + name
            l = len(queue_in+".")
            print("Listening on queue:", queue_in)
            sub_in = await js.subscribe(queue_in+".>",
                                        queue=self.queue+"-"+name,
                                        stream=self.queue)
            self._subs_in[name] = sub_in
        
        queue_out = self.queue + "." + self.outputs_name[0]
        print("Sending to queue:", queue_out)
        data_store = await js.object_store(bucket=self.queue+"-data")

        async def get_data(msg):
            uid = msg.subject[l:]
            source = msg.headers.get("DataSource", "")
            params_lst = msg.headers.get("Parameters", "")
            params = {}
            for p in params_lst.split(","):
                k, v = p.split("=")
                params[k] = v
            data = None
            if source == "json":
                data = loads(msg.data.decode())
            elif source == "object_store":
                obj_res = await data_store.get(msg.data.decode())
                data = obj_res.data
            elif source == "file":
                file = io.BytesIO()
                obj_res = await data_store.get(msg.data.decode(), file)
                file.read()
            else:
                data = msg.data

            return (uid, source, data, params)

        async def send_reply(uid, source, data, error=""):
            _out = queue_out + "." + uid
            breply = b''
            if data is not None:
                match source:
                    case "json":
                        breply = str(dumps(data)).encode()
                    case "object_store":
                        uid = str(uuid.uuid4())
                        breply = uid.encode()
                        await data_store.put(uid, data)
                    case "bytes":
                        breply = data
                    case _:
                        if isinstance(data, (bytes, bytearray)):
                            breply = data
                        else:
                            breply = (str(data)).encode()
            await js.publish(_out, breply, headers={"ProcessError": error, "DataSource": source})

        async def handle_msg(name, msgs, is_batch: bool):
            if is_batch:
                batch, uids, sources, params_lst = zip(*[await get_data(msg) for msg in msgs])
                batch = list(batch)
                reply, err = self._process_data(name, batch, params_lst, is_batch)
                if not err:
                    for data, uid, source in zip(reply, uids, sources):
                        await send_reply(uid, source, data)
                    return
                for uid, source in zip(uids, sources):
                    await send_reply(uid, source, None, err)
                return

            for msg in msgs:
                uid, source, data, params = await get_data(msg)
                reply, err = self._process_data(name, [data], [params], is_batch)
                if err:
                    await send_reply(uid, source, reply, err)
                else:
                    await send_reply(uid, source, reply[0])
                return

        async def term_msg(msgs):
            for msg in msgs:
                await msg.ack()

        async def wait_msg(name, sub_in):
            # Fetch and ack messagess from consumer.
            while True:
                try:
                    pending_msgs = sub_in.pending_msgs
                    if self.batch == 1 or pending_msgs == 0:
                        msg = await sub_in.next_msg(timeout=600)
                        await asyncio.gather(
                            handle_msg(name, [msg], False),
                            term_msg([msg])
                        )
                    else:
                        if pending_msgs >= self.batch:
                            _batch = self.batch
                        else:
                            _batch = pending_msgs
                        msgs = []
                        done = False
                        i = 0
                        while not done:
                            try:
                                msg = await sub_in.next_msg(timeout=0.01)
                                msgs.append(msg)
                            except TimeoutError:
                                done = True
                            i += 1
                            if i == _batch:
                                done = True
                            p = sub_in.pending_msgs
                            if p == 0:
                                done = True
                            elif p < _batch - i:
                                _batch = p + i

                        await asyncio.gather(
                            handle_msg(name, msgs, True),
                            term_msg(msgs)
                        )
                except NATSTimeoutError:
                    continue
                except TimeoutError:
                    continue
                except Exception as e: # pylint: disable=W0703
                    LOGGER.error("Fatal error message handler: %s",
                                str(e), exc_info=True)
                    break
        
        os.system("touch /tmp/running")
        tasks = []
        for name, sub_in in self._subs_in.items():
            tasks.append(wait_msg(name, sub_in))
        await asyncio.gather(*tasks)
        await nc.close()

    def _process_data(self, name: str, requests: list, reqs_parameters: list, is_batch: bool = False) -> Tuple[list, str | None]:
        """
        Process data
        Arguments:
        - requests:   list of data to process
        - is_batch:   is batched data
        Returns:
        - Tuple[List[bytes], str]:  list of processed data and error message
        """
        try:
            LOGGER.debug("handle request")
            data = [DataHandler(req, reqs_parameters, self.inputs[name], is_input=True) for req in requests]
            
            if is_batch:
                
                if self.callback_has_parameters:
                    result = self.callback(requests, reqs_parameters)
                else:
                    result = self.callback(requests)
                if not isinstance(result, list):    
                    return [], "batch reply is not a list"
                if len(requests) != len(result):
                    return [], "batch reply has wrong size"
            else:
                if len(requests) == 0:
                    request = []
                else:
                    request = requests[0]
                if len(reqs_parameters) == 0:
                    parameters = {}
                else:
                    parameters = reqs_parameters[0]
                if self.callback_has_parameters:
                    result = self.callback(request, parameters)
                else:
                    result = self.callback(request)
            return result, None
        except ValueError:
            LOGGER.error("Fatal error message handler", exc_info=True)
            return [], "Wrong input"
        except Exception as e: # pylint: disable=W0703
            LOGGER.error("Fatal error message handler", exc_info=True)
            return [], str(e)
