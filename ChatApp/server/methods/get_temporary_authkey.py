from ChatApp.utils.gen_crc_32 import CRC
from ..errors.bad_request import BadRequest
from ChatApp.utils.gen_auth_key import gen_auth_key
from ChatApp.database.create_db import AuthKey


class GetTemporaryAuthKey(metaclass=CRC, retval=1):
    __aqualname__ = "methods.GetTemporaryAuthKey"

    def __init__(self) -> bytes: pass

    @staticmethod
    def handle(data, protocol):
        if data:
            return protocol.send(BadRequest("Bad Packet").bytes)
        authkey = gen_auth_key()
        AuthKey(auth_key=authkey)
        return protocol.send(authkey)
