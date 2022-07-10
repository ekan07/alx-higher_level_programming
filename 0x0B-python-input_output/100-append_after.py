#!/usr/bin/python3
"""Module 100-append_after.
Inserts a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """Appends the new_string after
    the search_string in filename.
    Args:
        filename: name of the file
        search_string: string to append after
        new_string: new_string to append
    """
    with open(filename, "r", encoding="utf-8") as f:
        text = f.readlines()

    with open(filename, "w", encoding="utf-8") as f:
        for line in text:
            if search_string in line:
                line = line + new_string
            f.write(line)
