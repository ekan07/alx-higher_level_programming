#!/usr/bin/python3
"""Define a class Square(size).

If size is not an integer, raise TypeError.
If size is less than zero, raise ValueError.
"""


class Square:
    """Class that define a Square."""

    def __init__(self, size=0):
        """Initialize instance of square.
        Args:
            size (int): size of square.
        Raises:
            TypeError: if size is not integer.
            ValueError: if size is less than zero.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
