import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class FunctionStore: ...

class ReturnStore:
    """tuple() -> empty tuple
    tuple(iterable) -> tuple initialized from iterable's itemsIf the argument is a tuple, the return value is the same object.
    """

    def count(self):
        """T.count(value) -> integer -- return number of occurrences of value"""
        ...

    def index(self):
        """T.index(value, [start, [stop]]) -> integer -- return first index of value.
        Raises ValueError if the value is not present.

        """
        ...

def fromxml(data): ...
def tag_module(mod_name, tags): ...
def tag_vars(tags, module="bpyml"): ...
def topretty_py(py_data, indent="    "): ...
def toxml(py_data, indent="    "): ...
