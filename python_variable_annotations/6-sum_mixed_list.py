#!/usr/bin/env python3
"""Functions with simple variable annotations"""


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Function that add up all members of a list of ints & floats"""
    return float(sum(mxd_list))
