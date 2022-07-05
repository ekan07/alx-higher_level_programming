#!/usr/bin/python3
"""Module inherits_from"""

def inherits_from(obj, a_class):
    """
    Args
        obj: object
        a_class: class
    Return: True or False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
