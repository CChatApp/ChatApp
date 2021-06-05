from abc import ABC, abstractmethod


class Bytes(ABC):
    @abstractmethod
    def write(self):
        return NotImplemented

    @property
    def bytes(self):
        return self.write().encode()
