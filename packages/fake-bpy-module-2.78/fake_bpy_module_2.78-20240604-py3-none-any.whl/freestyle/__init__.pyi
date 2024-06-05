"""
This module provides data types of view map components (0D and 1D
elements), base classes for defining line stylization rules
(predicates, functions, chaining iterators, and stroke shaders), as
well as helper functions for style module writing.

Submodules:

* freestyle.types
* freestyle.predicates
* freestyle.functions
* freestyle.chainingiterators
* freestyle.shaders
* freestyle.utils

"""

import typing
import collections.abc
from . import chainingiterators
from . import functions
from . import predicates
from . import shaders
from . import types
from . import utils

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")
