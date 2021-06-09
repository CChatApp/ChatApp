from ChatApp.utils.gen_crc_32 import CRC
from ChatApp.server.methods.get_pg import GetPG
from ChatApp.server.methods.get_schama import GetSchema


class Meta(CRC):
    def __new__(mcs, *args, **kwargs):
        cls = super().__new__(mcs, *args, **kwargs)
        for i in cls.__bases__:
            cls.HANDLERS[int(i.ID, 16)] = i.handle
        return cls


class Mix(
    GetPG,
    GetSchema,
    metaclass=Meta
):
    __ignore_schema__ = True
    HANDLERS = {}
