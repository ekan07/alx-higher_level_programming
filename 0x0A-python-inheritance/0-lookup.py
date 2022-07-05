#!/usr/bin/python3
"""
Module 0-lookup
"""

def lookup(obj):
    """
    Args:
        obj: object to lookup to.
    Return: the list of available attributes and methods of an object.
    """
    return dir(obj)
