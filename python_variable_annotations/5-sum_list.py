#!/usr/bin/env python3
"""Functions with simple variable annotations"""


def sum_list(input_list: list[float]) -> float:
    """Function that add up all members of a list of floats"""
    return float(sum(input_list))
