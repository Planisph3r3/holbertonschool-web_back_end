#!/usr/bin/env python3
"""Functions with simple variable annotations"""


from math import floor


def concat(n: float) -> int:
    """Function that rounds down a float and returns an int"""
    return floor(n)
