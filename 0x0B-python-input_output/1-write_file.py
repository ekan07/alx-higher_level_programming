"""Module 3-write_file.
Writes in a text file.
"""


def write_file(filename="", text=""):
    """Writes text in filename.
    Args:
        - filename: name of the file
        - text: string to write in the file
    Returns: number of characters written
    """
    char_count = 0
    with open(filename, 'w+', encoding="utf-8") as f:
        char_count = f.write(text)
    return char_count
