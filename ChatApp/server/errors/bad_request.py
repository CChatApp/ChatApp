from __future__ import annotations
from ChatApp.utils.gen_crc_32 import CRC
from ChatApp.utils.bytes import Bytes


class BadRequest(Bytes, metaclass=CRC, desc=1, retval=1):
    CODE = 400
    __qualname__ = "BadRequest"

    def __init__(self, desc: str) -> BadRequest:
        self.desc = desc

    def write(self):
        return self.__class__.__name__ + "_" + str(self.CODE) + ":" + self.desc
