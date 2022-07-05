#!/usr/bin/python3
"""Module is_kind_of_class"""

def is_kind_of_class(obj, a_class):
    """
    is_same_class determines if is an instance of class.
    Args:
        obj: object to look at.
        a_class: class to verify the instance of.
    Returns: True if obj is an instance of a_class,
    or if the object is an instance of a class that
    inherited from, the specified class; False otherwise
    """
    return isinstance(obj, a_class)
