#!/usr/bin/python3
"""
Module add-integer
Adds two integer together
"""


def add_integer(a, b=98):
    """
    Adds two integer.
    Args:
        a (int|float): An integer or floating point number
        b (int|float): An integer or floating point number
    Returns: The sum of `a` and `b`
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    else:
        return (int(a) + int(b))
