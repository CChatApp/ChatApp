from binascii import crc32
from abc import ABCMeta
from .gen_signature import gen_signature


class CRC(ABCMeta):
    def __new__(mcs, *args, **kwargs):
        cls = super().__new__(mcs, *args)
        signature, n = gen_signature(cls, **kwargs)
        if not getattr(cls, "ID", None):
            cls.ID = hex(crc32((cls.__qualname__ + "@" + signature).encode()))
        cls.signature = cls.__qualname__ + "#" + cls.ID + (" " if n else "") + signature
        cls.signature_obj = gen_signature(cls, **kwargs, _obj=True)
        return cls
