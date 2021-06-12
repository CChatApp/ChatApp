from unittest import TestCase
from ChatApp.utils.gen_signature import gen_signature
from ChatApp.utils.signatures import Arg, Signature


class TestGenSignature(TestCase):
    def test_gen_signature(self):
        def func(a, b: int, c: str = "hello", d: TestCase = True) -> bool: pass
        self.assertEqual(gen_signature(func, a=1, b=1, c=1, d=1, retval=1)[0],
                         "a b:int c:str='hello' d:TestCase=True -> bool")
        self.assertEqual(gen_signature(func, a=1, b=1, c=1, d=1)[0],
                         "a b:int c:str='hello' d:TestCase=True -> <class 'bool'>")
        self.assertEqual(gen_signature(func, a=1, b=1, d=1)[0],
                         "a b:int c:<class 'str'>='hello' d:TestCase=True -> <class 'bool'>")
        self.assertEqual(gen_signature(func, a=1, b=1, d=1, _obj=True),
                         Signature(args=[
                             Arg(name="a", annotation=None, default=None),
                             Arg(name="b", annotation="int", default=None),
                             Arg(name="c", annotation="<class 'str'>", default="'hello'"),
                             Arg(name="d", annotation="TestCase", default="True"),
                         ], return_value="<class 'bool'>"))
        self.assertEqual(gen_signature(func, a=1, b=1, c=1, d=1, retval=1, _obj=True),
                         Signature(args=[
                             Arg(name="a", annotation=None, default=None),
                             Arg(name="b", annotation="int", default=None),
                             Arg(name="c", annotation="str", default="'hello'"),
                             Arg(name="d", annotation="TestCase", default="True"),
                         ], return_value="bool"))
