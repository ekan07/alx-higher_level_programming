#!/usr/bin/python3
"""Module 2-is_same_class"""


def is_same_class(obj, a_class):
    """
    is_same_class determines if is an instance of class.
    Args:
        obj: object to look at.
        a_class: class to verify the instance of.
    Returns: True if obj is an instance of a_class,
    False otherwise
    """
    return True if type(obj) is a_class else False
