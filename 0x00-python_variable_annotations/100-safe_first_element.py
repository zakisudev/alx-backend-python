#!/usr/bin/env python3
"""Module for safe_first_element function"""
from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Function that returns the first element of a sequence or None.
    
    Args:
        lst (Sequence[Any]): The sequence.

    Returns:
        Union[Any, None]: The first element of the sequence or None.
    """
    if lst:
        return lst[0]
    else:
        return None