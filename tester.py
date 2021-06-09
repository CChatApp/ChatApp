import unittest
import datetime


class TextTestResult(unittest.TextTestResult):
    def startTest(self, test):
        if self.showAll:
            self.stream.write(f"[{datetime.datetime.now()}] ")
            self.stream.write(self.getDescription(test))
            self.stream.write(" ... ")
            self.stream.flush()


class Loader(unittest.TestProgram):
    def createTests(self, from_discovery=False, Loader=None):
        loader = self.testLoader if Loader is None else Loader()
        self.test = loader.discover("tests", "test*.py", ".")


unittest.TextTestRunner.resultclass = TextTestResult
Loader(verbosity=2)
