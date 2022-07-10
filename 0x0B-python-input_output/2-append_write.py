#!/usr/bin/python3
"""Module 4-append_write.
Appends a string at the end of a text file.
"""


def append_write(filename="", text=""):
    """Appends text to filename.
    Args:
        - filename: name of the file
        - text: text to append
    Returns: the number of characters added
    """
    char_count = 0
    with open(filename, 'a', encoding="utf-8") as f:
        char_count = f.write(text)
    return char_count
