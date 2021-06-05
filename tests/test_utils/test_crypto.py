from unittest import TestCase
from ChatApp.utils.crypto import generate_pg, is_prime, find_primitive


class TestCrypto(TestCase):
    def _test_generate_pg(self):
        gs = {2, 3, 4, 5, 6, 7}
        already = set()
        while already != gs:
            p, g = generate_pg()
            self.assertIn(g, gs)
            self.assertTrue(is_prime(p))
            self.assertEqual(find_primitive(p), g)
            already.add(g)
            print(already)