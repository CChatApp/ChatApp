from pyDH import DiffieHellman
from ChatApp.utils.gen_crc_32 import CRC
from ..errors.bad_request import BadRequest
from ..types.pg import PG


def int_to_bytes(i: int, *, signed: bool = False) -> bytes:
    length = ((i + ((i * signed) < 0)).bit_length() + 7 + signed) // 8
    return i.to_bytes(length, byteorder='big', signed=signed)


class GetPG(metaclass=CRC, retval=1):
    def __init__(self) -> "types.PG": pass

    @staticmethod
    def handle(data, transport):
        dh = DiffieHellman()
        if data:
            return transport.write(BadRequest("Bad Packet").bytes)
        transport.write(PG(int_to_bytes(dh.p), int_to_bytes(dh.g)).bytes)
