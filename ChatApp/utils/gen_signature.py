from inspect import signature, _empty as empty
from .signatures import Signature, Arg


def gen_signature(_c, _obj: bool = False, **kwargs):
    sign = signature(_c)
    params = [p for p in sign.parameters.values()]
    f_signature = Signature()
    for p in params:
        arg = Arg(p.name)
        if p.annotation != empty:
            if kwargs.get(p.name) == 1:
                arg.annotation = str(p.annotation) if not getattr(p.annotation, "__qualname__", None) else p.annotation.__name__
            else:
                arg.annotation = repr(p.annotation)
        if p.default != empty:
            arg.default = (
                repr(p.default) if isinstance(p.default, str) else str(p.default)
                if not getattr(p.default, "__qualname__", None) else p.default.__name__
            )
        f_signature.args.append(arg)
    if sign.return_annotation != empty:
        if kwargs.get("retval") == 1:
            f_signature.return_value = (str(sign.return_annotation)
                if not getattr(sign.return_annotation, "__qualname__", None)
                else sign.return_annotation.__qualname__)
        else:
            f_signature.return_value = repr(sign.return_annotation)
    if not _obj:
        return str(f_signature), len(params)
    return f_signature
