#!/usr/bin/python3
"""Module 0-read_file.
"""


def read_file(filename=""):
    """Reads from filename and prints
    its contents to stdout.
    Args:
        - filename: name of the file
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
