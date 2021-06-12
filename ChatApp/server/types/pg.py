from ChatApp.utils.gen_crc_32 import CRC
from ChatApp.utils.bytes import Bytes


class PG(Bytes, metaclass=CRC, p=1, g=1, retval=1):
    __qualname__ = "types.PG"

    def __init__(self, p: bytes, g: bytes) -> __qualname__:
        self.p = p
        self.g = g

    def write(self):
        return f"{PG.__qualname__}({self.p}, {self.g})"
