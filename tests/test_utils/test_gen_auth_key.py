from unittest import TestCase
from ChatApp.utils.gen_auth_key import gen_auth_key


class TestGenAuthKey(TestCase):
    def test_gen_auth_key(self):
        for i in range(999):
            self.assertIsInstance(gen_auth_key(), bytes)
