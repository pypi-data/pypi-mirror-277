import importlib
import importlib.util
from functools import reduce
from types import ModuleType
from typing import Any, Iterable, Union

MODULE_DTYPE = {
    "numpy": "ndarray",
    "torch": "Tensor",
    "tensorflow": "Tensor",
}

MODULE_TYPECAST = {
    "numpy": "asarray",
    "torch": "as_tensor",
    "tensorflow": "Variable",
}


def cast_to_dtype(object: Any, module: str, **kwargs):
    """Casts the object to the basic data type associated with the module"""
    if not module in MODULES:
        raise ValueError(f"{module} is not a valid module")
    return get_module_attr(module, MODULE_TYPECAST[module])(object, **kwargs)


def deepgetattr(obj: ModuleType, attr: str):
    return reduce(getattr, attr.split("."), obj)


def get_module_dtype(module: str) -> Any:
    if not module in MODULES:
        raise Exception(f"{module} not a valid module")
    return get_module_attr(module, MODULE_DTYPE[module])


def get_module_from_object(object: Any, default: str) -> str:
    for module in MODULES:
        if is_module_dtype(object, module):
            return module
    return default


def get_module_from_objects(objects: Iterable[Any], default: str) -> str:
    modules = set([get_module_from_object(object, default) for object in objects])
    if len(modules) > 1:
        raise ValueError(f"Multiple data types found: {modules}")
    return modules.pop()


def get_module_attr(module: str, attr: str) -> Any:
    """Returns the attr associated with the module"""
    return deepgetattr(get_module(module), attr)


def get_module(module: str) -> ModuleType:
    """
    Returns the module object if the module is installed,
    otherwise raises an ModuleNotFoundError.
    """
    if is_module_installed(module):
        return importlib.import_module(module)
    else:
        raise ModuleNotFoundError(f"Module `{module}` was not found")


def is_module_installed(module: str) -> bool:
    """Checks if a module is installed."""
    return importlib.util.find_spec(module) is not None


def is_module_dtype(object: Any, module: str) -> bool:
    """Determines if the object is an instance of the module"""
    if not module in MODULES:
        raise Exception(f"{module} not a valid module")
    return isinstance(object, get_module_dtype(module))


DEFAULT_MODULE = None
MODULES = []
for module, dtype in MODULE_DTYPE.items():
    if is_module_installed(module):
        if DEFAULT_MODULE is None:
            DEFAULT_MODULE = module
        importlib.import_module(module)
        MODULES.append(module)

if DEFAULT_MODULE is None:
    raise AttributeError(
        f"Please install at least one of the following modules: {[x for x in MODULE_DTYPE.keys()]}"
    )

TYPEHINT_DTYPE = Union[tuple(get_module_dtype(module) for module in MODULES)]
TYPEHINT_MODULE = Union[tuple(MODULES)]
