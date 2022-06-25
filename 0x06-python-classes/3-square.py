#!/usr/bin/python3
"""Square(size)

Calculates the area of a square from the given size.
Returns the calculated area.

If size is not an integer, raise TypeError.
If size is less than zero, raise ValueError.
"""


class Square:
    """class that define a Square."""

    def __init__(self, size=0):
        """Initializes instance of square.
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
        """compute area of square
        Returns:
            the current square area
        """
        return(self.__size ** 2)
