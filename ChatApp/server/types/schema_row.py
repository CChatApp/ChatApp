from ChatApp.utils.gen_crc_32 import CRC
from ChatApp.utils.bytes import Bytes
from ChatApp.server.types.schema_param import SchemaArg
from typing import List


class SchemaRow(Bytes, metaclass=CRC, name=1, id=1, retval=1):
    __qualname__ = "types.SchemaRow"

    def __init__(self, name: str, id: str, params: List[SchemaArg] = []) -> __qualname__:
        self.name = name
        self.id = id
        self.params = params

    def write(self):
        params = [SchemaArg(p.name, p.annotation, p.default).write() for p in self.params]
        return f'{SchemaRow.__qualname__}({self.name}, {self.id}, [{", ".join(params)}])'
