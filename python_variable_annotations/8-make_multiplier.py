#!/usr/bin/env python3
"""Functions with complex variable annotations"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    A function that takes a float multiplier
    as argument and returns a
    function that multiplies a float by multiplier
    """

    def multiplier_func(n: float) -> float:
        return float(n * multiplier)

    return multiplier_func
