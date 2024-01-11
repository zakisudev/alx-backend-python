#!/usr/bin/env python3
"""Module for to_kv function"""
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function that returns a tuple with a string and the square of a number.
    
    Args:
        k (str): The string.
        v (Union[int, float]): The number.

    Returns:
        Tuple[str, float]: The tuple with the string and the square of the number.
    """
    return k, v**2