#!/usr/bin/env python3
"""Module for element_length function"""
from typing import List, Tuple, Iterable, Sequence

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that returns a list of tuples, each containing a sequence and its length.
    
    Args:
        lst (Iterable[Sequence]): The iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: The list of tuples.
    """
    return [(i, len(i)) for i in lst]