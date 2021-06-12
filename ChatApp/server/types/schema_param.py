from ChatApp.utils.gen_crc_32 import CRC
from ChatApp.utils.bytes import Bytes
from typing import Any


class SchemaArg(Bytes, metaclass=CRC, name=1, type=1, default=1, retval=1):
    __qualname__ = "types.SchemaArg"

    def __init__(self, name: str, type: str, default: Any = None) -> __qualname__:
        self.name = name
        self.type = type
        self.default = default

    def write(self):
        return f'{SchemaArg.__qualname__}("{self.name}", {self.type}, {self.default})'
