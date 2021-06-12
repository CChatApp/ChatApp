from ChatApp.utils.gen_crc_32 import CRC
from ChatApp.utils.bytes import Bytes


class IPIsBlocked(Bytes, metaclass=CRC, desc=1, retval=1):
    CODE = 403
    __qualname__ = "errors.IPIsBlocked"

    def __init__(self, desc: str) -> __qualname__:
        self.desc = desc

    def write(self):
        return self.__class__.__name__ + "_" + str(self.CODE) + ":" + self.desc
