from ChatApp.utils.gen_crc_32 import CRC
from ChatApp.utils.bytes import Bytes


class PG(Bytes, metaclass=CRC, p=1, g=1, retval=1):
    def __init__(self, p: bytes, g: bytes) -> "PG":
        self.p = p
        self.g = g

    def write(self):
        return "PG({}, {})".format(self.p, self.g)
