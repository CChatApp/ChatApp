from ChatApp.utils.gen_crc_32 import CRC
from ..errors.bad_request import BadRequest
from ..types.schema import Schema
from ChatApp import schema, layer


class GetSchema(metaclass=CRC, retval=1):
    def __init__(self) -> "types.Schema": pass

    ID = hex(0x12345678)

    @staticmethod
    def handle(data, transport):
        if data:
            return transport.write(BadRequest("Bad Packet").bytes)

        return transport.write(Schema(";".join(schema), layer).bytes)
