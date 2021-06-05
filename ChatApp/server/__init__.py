from ..utils.gen_crc_32 import CRC
from ChatApp.server.methods.get_pg import GetPG


class Meta(CRC):
    def __new__(mcs, *args, **kwargs):
        cls = super().__new__(mcs, *args, **kwargs)
        for i in cls.__bases__:
            cls.HANDLERS[int(i.ID, 16)] = i.handle
        return cls


class Mix(
    GetPG,
    metaclass=Meta
):
    HANDLERS = {}
