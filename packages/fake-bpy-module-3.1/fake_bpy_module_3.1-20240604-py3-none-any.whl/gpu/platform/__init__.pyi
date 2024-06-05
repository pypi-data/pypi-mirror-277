"""
This module provides access to GPU Platform definitions.

"""

import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def renderer_get() -> str:
    """Get GPU to be used for rendering.

    :return: GPU name.
    :rtype: str
    """

    ...

def vendor_get() -> str:
    """Get GPU vendor.

    :return: Vendor name.
    :rtype: str
    """

    ...

def version_get() -> str:
    """Get GPU driver version.

    :return: Driver version.
    :rtype: str
    """

    ...
