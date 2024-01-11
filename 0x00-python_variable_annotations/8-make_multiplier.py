#!/usr/bin/env python3
"""Module for make_multiplier function"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function that returns a function that multiplies a float by a given multiplier.
    
    Args:
        multiplier (float): The multiplier.

    Returns:
        Callable[[float], float]: The function that multiplies a float by the multiplier.
    """
    def multiplier_func(n: float) -> float:
        return n * multiplier
    return multiplier_func