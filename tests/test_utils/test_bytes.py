from unittest import TestCase, main
from ChatApp.utils.bytes import Bytes


class TestBytes(TestCase):
    def test_bytes(self):
        class A(Bytes):
            pass
        self.assertRaises(TypeError, A)

