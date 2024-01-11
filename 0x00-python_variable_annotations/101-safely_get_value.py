#!/usr/bin/env python3
"""Module for safely_get_value function"""
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Function that returns the value corresponding to a key in a mapping or a default value.
    
    Args:
        dct (Mapping): The mapping.
        key (Any): The key.
        default (Union[T, None]): The default value.

    Returns:
        Union[Any, T]: The value corresponding to the key in the mapping or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default