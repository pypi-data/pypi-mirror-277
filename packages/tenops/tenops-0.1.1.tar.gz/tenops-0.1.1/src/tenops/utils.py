from collections import defaultdict
from typing import Any


class ParameterAlias:
    """
    Class for transforming parameter names to the appropriate name for a module.

    Parameters
    ----------
    params : dict[str, Any]
        A dictionary containing the key-value pairs for the function.


    **kwargs : dict[str,str]
        Arguments where the keyword is the parameter name and the value a dictionary
        whose key is the module name and value is the parameter associated with the
        module. So, for example, in PyTorch the axis parameter is represented by "dim"
        so one would pass in the following:

            axis = {"torch": "dim"}

    Examples
    --------
    >>> from dops.utils import Parameter
    >>> p = Parameter(params={"axis": 0}, axis={"torch": "dim"})
    >>> p["torch"]
    {"dim": 1}
    """

    def __init__(self, params: dict[str, Any], **kwargs: dict[str, str]):
        self.params = params
        self.alias = {k: defaultdict(lambda: k) for k in params.keys()}
        for param, item in kwargs.items():
            for module, func in item.items():
                self.alias[param][module] = func

    def __getitem__(self, module: str) -> str:
        return {self.alias[k][module]: v for k, v in self.params.items()}
