#!/usr/bin/env python3
"""
Write a type-annotated function sum_mixed_list whichntakes a list
mxd_lst on integers and floats and returns their sum as float
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Returns the sum of the list as a float"""
    return float(sum(mxd_lst))
