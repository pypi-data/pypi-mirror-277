from collections import defaultdict
from typing import Iterable, Union

from .manage import (
    DEFAULT_MODULE,
    TYPEHINT_DTYPE,
    TYPEHINT_MODULE,
    cast_to_dtype,
    get_module_attr,
    get_module_from_object,
    get_module_from_objects,
)
from .utils import ParameterAlias


def arange(
    *args: int, default: TYPEHINT_MODULE = DEFAULT_MODULE, **kwargs
) -> TYPEHINT_DTYPE:
    d = defaultdict(lambda: "arange")
    d["tensorflow"] = "range"
    return get_module_attr(default, d[default])(*args, **kwargs)


def cat(
    x: Iterable[TYPEHINT_DTYPE],
    default: TYPEHINT_MODULE = DEFAULT_MODULE,
    axis: int = 0,
    **kwargs
) -> TYPEHINT_DTYPE:
    d = defaultdict(lambda: "concatenate")
    d.update({"torch": "cat", "tensorflow": "concat"})

    p = ParameterAlias(params={"axis": axis}, axis={"torch": "dim"})
    module = get_module_from_objects(x, default=default)
    x = [cast_to_dtype(xi, module=module) for xi in x]
    return get_module_attr(module, d[module])(x, **p[module], **kwargs)


def empty_like(
    x: TYPEHINT_DTYPE, default: TYPEHINT_MODULE = DEFAULT_MODULE, **kwargs
) -> TYPEHINT_DTYPE:
    d = defaultdict(lambda: "empty_like")
    d["tensorflow"] = "experimental.numpy.empty_like"
    module = get_module_from_object(x, default=default)
    x = cast_to_dtype(x, module=module)
    return get_module_attr(module, d[module])(x, **kwargs)


def linspace(
    *args: Union[int, float], default: TYPEHINT_MODULE = DEFAULT_MODULE, **kwargs
) -> TYPEHINT_DTYPE:
    d = defaultdict(lambda: "linspace")
    return get_module_attr(default, d[default])(*args, **kwargs)


def meshgrid(
    *x: TYPEHINT_DTYPE,
    indexing: str = "ij",
    default: TYPEHINT_MODULE = DEFAULT_MODULE,
    **kwargs
) -> tuple[TYPEHINT_DTYPE]:
    d = defaultdict(lambda: "meshgrid")
    p = ParameterAlias(params={"indexing": indexing})
    module = get_module_from_objects(x, default=default)
    x = [cast_to_dtype(xi, module=module) for xi in x]
    return get_module_attr(module, d[module])(*x, **p[module], **kwargs)


def reshape(
    x: TYPEHINT_DTYPE,
    shape: Iterable[int],
    default: TYPEHINT_MODULE = DEFAULT_MODULE,
    **kwargs
) -> TYPEHINT_DTYPE:
    d = defaultdict(lambda: "reshape")
    p = ParameterAlias(params={"shape": shape}, shape={"numpy": "newshape"})
    module = get_module_from_object(x, default=default)
    x = cast_to_dtype(x, module=module)
    return get_module_attr(module, d[module])(x, **p[module], **kwargs)


def stack(
    x: Iterable[TYPEHINT_DTYPE],
    default: TYPEHINT_MODULE = DEFAULT_MODULE,
    axis: int = 1,
    **kwargs
) -> TYPEHINT_DTYPE:
    d = defaultdict(lambda: "stack")
    p = ParameterAlias(params={"axis": axis}, axis={"torch": "dim"})
    module = get_module_from_objects(x, default=default)
    x = [cast_to_dtype(xi, module=module) for xi in x]
    return get_module_attr(module, d[module])(x, **p[module], **kwargs)


def zeros_like(
    x: TYPEHINT_DTYPE, default: TYPEHINT_MODULE = DEFAULT_MODULE, **kwargs
) -> TYPEHINT_DTYPE:
    d = defaultdict(lambda: "zeros_like")
    module = get_module_from_object(x, default=default)
    x = cast_to_dtype(x, module=module)
    return get_module_attr(module, d[module])(x, **kwargs)


# Alias
concat = cat
concatenate = cat
