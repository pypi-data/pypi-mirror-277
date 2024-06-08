"""
IA Parc Inference data handler
"""
import os
import io
import logging
import logging.config
from typing import Image, BytesIO, Audio, Any

LEVEL = os.environ.get('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(
    level=LEVEL,
    force=True,
    format="%(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
LOGGER = logging.getLogger("Inference")
LOGGER.propagate = True


class DataHandler():
    """
    Data Handler
    This a read-only class that handles the data
    """

    def __init__(self, data: bytes, parameters: dict, conf: dict, is_input: bool = True):
        """
        Constructor
        Arguments:
        
        """
        self._raw = data
        self._conf = conf
        self._name = conf["name"]
        self._parameters = parameters
        self._items = {}       
        ## Init to None data kinds
        self._file: BytesIO = None
        self._text: str = None
        self._image: Image = None
        #self._audio = None
        #self._video = None
        self._json: dict = None
        #self._table = None
        self._is_multi = self._conf["type"] == "multimodal"
        if not is_input:
            self.encode = self._encode
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def items(self) -> dict:
        if self._is_multi:
            if not self._items:
                self._items = _read_multi_part(self._raw, self._conf["items"])
            return self._items
        else:
            if not self._items:
                self._items[self.name] = self
            return self._items
    
    @property
    def raw(self) -> bytes:
        return self._raw
    @property
    def parameters(self) -> dict:
        return self._parameters
    
    @property
    def file(self) -> BytesIO:
        if self._is_multi or self._conf["type"] not in ["file", "image", "binary", "audio", "video"]:
            return None
        if not self._file:
            self._file = _read_file(self._raw)
        return self._file
        
    @property
    def text(self) -> str:
        if self._is_multi or self._conf["type"] != "text":
            return None
        if not self._text:
            self._text = _read_text(self._raw)
        return self._text
    
    @property
    def image(self) -> Image:
        if self._is_multi or self._conf["type"] != "image":
            return None
        if not self._image:
            self._image = _read_image(self._raw)
        return self._image
    
    @property
    def json(self) -> dict:
        if self._is_multi or self._conf["type"] != "json":
            return None
        if not self._json:
            self._json = _read_json(self._raw)
        return self._json

    def _encode(self, data: Any) -> tuple[ValueError, bytes]:
        """
        Encode data
        Arguments:
        data: Any
        """
        if not data:
            return ValueError("Data is empty"), None
        return data


## Data readers

def _read_file(data: bytes) -> BytesIO:
    """
    Read file
    Arguments:
    data: bytes
    """
    file = io.BytesIO(data)
    return file

def _read_image(data: bytes) -> Image:
    """
    Read image
    Arguments:
    data: bytes
    """
    from PIL import Image
    image = Image.open(io.BytesIO(data))
    return image

def _read_text(data: bytes) -> str:
    """
    Read text
    Arguments:
    data: bytes
    """
    text = data.decode("utf-8")
    return text

def _read_json(data: bytes) -> dict:
    """
    Read json
    Arguments:
    data: bytes
    """
    import json
    json_data = json.loads(data)
    return json_data
    
def _read_multi_part(data: bytes, items: list) -> dict:
    """
    Read multi-part data
    Arguments:
    data: bytes
    """
    from streaming_form_data import StreamingFormDataParser
    from streaming_form_data.targets import BaseTarget

    class BytesTarget(BaseTarget):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._data = None
            
        def on_data_received(self, data: bytes):
            self.data = data

    results = {}

    headers = {'Content-Type': 'multipart/form-data; boundary=boundary'}
    parser = StreamingFormDataParser(headers=headers)
    for item in items:
        results[item["name"]] = BytesTarget()                
        parser.register(item["name"], results[item["name"]])

    parser.data_received(data)
    
    for item in items:
        results[item["name"]] = DataHandler(results[item["name"]].data, {}, item, True)
    
    return results        


def _read_audio(data: bytes) -> Audio:
    """
    Read audio
    Arguments:
    data: bytes
    """
    pass