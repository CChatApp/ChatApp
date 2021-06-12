from dataclasses import dataclass, field
from typing import List, Any


@dataclass
class Arg:
    name: str
    annotation: Any = None
    default: Any = None

    def __str__(self):
        return self.name + ((":" + self.annotation) if self.annotation else "") + (("=" + self.default) if self.default else "")


@dataclass
class Signature:
    args: List[Arg] = field(default_factory=list)
    return_value: Any = None

    def __str__(self):
        return " ".join(map(str, self.args)) + ((" -> " + self.return_value) if self.return_value else "")
