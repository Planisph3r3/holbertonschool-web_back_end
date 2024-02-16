#!/usr/bin/env python3
"""Functions with simple variable annotations"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function that that takes a string k and an int OR float v
    as arguments and returns a tuple.
    """
    return  (k, v ** 2)
