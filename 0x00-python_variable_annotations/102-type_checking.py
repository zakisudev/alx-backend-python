#!/usr/bin/env python3
"""Module for zoom_array function"""
from typing import List, Tuple

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Function that repeats each element of a tuple a number of times equal to a factor.
    
    Args:
        lst (Tuple): The tuple.
        factor (int): The factor.

    Returns:
        List: The list with repeated elements.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)