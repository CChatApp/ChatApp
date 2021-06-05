from unittest import TestCase
from ChatApp.utils.gen_crc_32 import CRC


class TestCRC(TestCase):
    def test_CRC(self):
        class Test(metaclass=CRC, a=1, b=1):
            __qualname__ = "Test"

            def __init__(self, a: int = 1, b: TestCase = False, c: str = "hello"):
                pass

        self.assertEqual(Test.ID, "0x21248c8d")
