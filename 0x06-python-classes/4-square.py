#!/usr/bin/python3
"""Square(size)

Calculates the area of a square from the given size.
Square(size).area() returns the calculated area.
Square(size).size to set/get the size.

If size is not an integer, raise TypeError.
If size is less than zero, raise ValueError.
"""


class Square:
    """Class that define a Square, computes square area."""
    def __init__(self, size=0):
        """Initializes instance of Square.
        Args:
            size: size of square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than zero.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Computes square area."""
        return(self.__size ** 2)

    @property
    def size(self):
        """Gets size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size.
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
