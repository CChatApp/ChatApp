from typing import _GenericAlias as GenericAlias, _type_repr as type_repr
from os import getcwd, path, walk
from importlib import import_module
from ChatApp.utils.gen_crc_32 import CRC
from pathlib import Path


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
                if isinstance(getattr(module, i), CRC):
                    s[Path(getattr(module, i).__module__).stem.split(".")[-1]].add(getattr(module, i))


with open(path.join(getcwd(), "schema"), "w") as f:
    f.write("// This file is generated automatically and uses types as in Python\n"
            "// For example, ``Tuple[int, int]`` is typing.Tuple, (int(), int()).\n"
            "// The CRC32 of each method is method name + @ + method signature, for instance: "
            "``PG@p:bytes g:bytes->PG`` will produce the CRC32 0x5323a87c\n\n")
    cls = {}
    for i in ("errors", "types", "methods"):
        cls[i] = set()
        visit(i, cls)
        f.write(f"////////////////////////////////////////////\n"
                f"/////////////      {i:>8}     ////////////\n"
                f"////////////////////////////////////////////\n")
        for c in cls[i]:
            f.write(c.signature + ";\n")
        f.write("\n")
