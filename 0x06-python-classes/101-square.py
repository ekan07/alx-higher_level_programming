#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """initializes square, determines size, calculates area, prints"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes instance of Square.
        Args:
            size: size of square
            position: position to indent square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """gets size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """gets position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """sets position
        Args:
            value: value of position
        Raises:
            TypeError: if position is not a tuple of 2 positive integers
        """
        if not (
                isinstance(value, tuple) and
                len(value) == 2 and
                isinstance(value[0], int) and
                isinstance(value[1], int) and
                value[0] >= 0 and value[1] >= 0):
            raise TypeError(
                "position musst be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Computes square area"""
        return (self.__size ** 2)

    def my_print(self):
        """prints square offsetting it by position with symbol #"""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print("{}{}".format(" " * self.__position[0], '#' * self.__size))

    def __str__(self):
        """prints square offsetting it by position with symbol #"""
        if self.__size == 0:
            return ""
        new_lines = "\n" * self.__position[1]
        spaces = " " * self.__position[0]
        hashes = "#" * self.__size
        return new_lines + "\n".join(spaces + hashes for i in range(self.size))
