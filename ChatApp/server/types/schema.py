from ChatApp.utils.gen_crc_32 import CRC
from ChatApp.utils.bytes import Bytes


class Schema(Bytes, metaclass=CRC, schema=1, layer=1, retval=1):
    def __init__(self, schema: str, layer: int) -> "types.Schema":
        self.schema = schema
        self.layer = layer

    def write(self):
        return f'types.Schema("{self.schema}",{self.layer})'
