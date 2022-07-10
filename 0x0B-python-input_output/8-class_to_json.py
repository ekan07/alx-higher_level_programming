#!/usr/bin/python3
"""Module 8-class_to_json"""


def class_to_json(obj):
    """Create a dict descrption of obj

    Args:
        obj: object to serialize
    """
    res = obj.__dict__
    return res
