from ChatApp.utils.gen_crc_32 import CRC
from ChatApp.utils.bytes import Bytes
from ChatApp.server.types.schema_row import SchemaRow


class Schema(Bytes, metaclass=CRC, schema=1, layer=1, retval=1):
    __qualname__ = "types.Schema"

    def __init__(self, schema: str, layer: int) -> __qualname__:
        self.schema = schema
        self.layer = layer

    def write(self):
        schema = [SchemaRow(row[0].__qualname__, row[0].ID, row[1].args).write() for row in self.schema]
        return f'{Schema.__qualname__}([{", ".join(schema)}],{self.layer})'
