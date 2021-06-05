from inspect import signature, _empty as empty


def gen_signature(_c, **kwargs):
    sign = signature(_c)
    params = [p for p in sign.parameters.values()]
    f_signature = ""
    for p in params:
        f_signature += p.name
        if p.annotation != empty:
            f_signature += ":"
            if kwargs.get(p.name) == 1:
                f_signature += str(p.annotation) if not getattr(p.annotation, "__qualname__", None) else p.annotation.__name__
            else:
                f_signature += repr(p.annotation)
        if p.default != empty:
            f_signature += "=" + (
                repr(p.default) if isinstance(p.default, str) else str(p.default)
                if not getattr(p.default, "__qualname__", None) else p.default.__name__
            )
        f_signature += " "
    f_signature = f_signature[:-1]
    if sign.return_annotation != empty:
        f_signature += "->"
        if kwargs.get("retval") == 1:
            f_signature += str(sign.return_annotation)\
                if not getattr(sign.return_annotation, "__qualname__", None)\
                else sign.return_annotation.__qualname__
        else:
            f_signature += repr(sign.return_annotation)

    return f_signature, len(params)
