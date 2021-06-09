from typing import _GenericAlias as GenericAlias, _type_repr as type_repr
from os import getcwd, path, walk, linesep
from importlib import import_module
from ChatApp.utils.gen_crc_32 import CRC
from pathlib import Path
from ChatApp.config import layer


def __repr__(self):
    if self._name:
        name = self._name
    else:
        name = type_repr(self.__origin__)
    args = ", ".join([type_repr(a) for a in self.__args__])
    return f'{name}[{args}]'


GenericAlias.__repr__ = __repr__


def visit(directory, s):
    for directory, dirs, files in walk(path.join(getcwd(), "ChatApp", "server", directory)):
        for file in files:
            if file.endswith("pyc"):
                continue
            module = import_module(path.relpath(directory, ".").replace("/", ".") + "." + file.replace(".py", ""))
            for i in dir(module):
                if getattr(getattr(module, i, None), "__ignore_schema__", None):
                    continue
                if isinstance(getattr(module, i), CRC):
                    s[Path(getattr(module, i).__module__).stem.split(".")[-1]].add(getattr(module, i))


schema = []

with open(path.join(getcwd(), "schema"), "w") as f:
    f.write(f"// ChatApp schema layer {layer}.{linesep}"
            f"// This file is generated automatically and uses types as in Python{linesep}"
            f"// For example, ``Tuple[int, int]`` is typing.Tuple, (int(), int()).{linesep}"
            "// The CRC32 of each method is method name + @ + method signature, for instance: "
            f"``PG@p:bytes g:bytes -> PG`` will produce the CRC32 0x45e27682{linesep}{linesep}")
    cls = {}
    for i in ("errors", "types", "methods"):
        cls[i] = set()
        visit(i, cls)
        f.write(f"////////////////////////////////////////////{linesep}"
                f"/////////////      {i:>8}     ////////////{linesep}"
                f"////////////////////////////////////////////{linesep}")
        for c in cls[i]:
            schema.append(i + "." + c.signature)
            f.write(i + "." + c.signature + f";{linesep}")
        f.write(linesep)
