#!/usr/bin/pyhon3
"""Module rectangle.
Create a Rectangle class, inheriting from Base.
"""
from typing import Type
from .base import Base


class Rectangle(Base):
    """Class describing a rectangle.
    Public instance methods:
        - area()
        - display()
        - to_dictionary()
        - update()
    Inherits from Base.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance.
        Args:
            - __width: width
            - __height: height
            - __x: position
            - __y: position
            - id: id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def integer_validator(self, name, value):
        """integer_validator
        Raises:
            TypeError: if value is not an integer.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    def x_y_validator(self, name, value):
        """x_y_validator
        Raises:
            ValueError: if value is less than 0.
        """
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """Retrieves width attribute."""
        return self.__width

    @property
    def height(self):
        """Retrieves height attribute."""
        return self.__height

    @property
    def x(self):
        """Retrieves x attribute."""
        return self.__x

    @property
    def y(self):
        """Retrieves y attribute."""
        return self.__y

    @width.setter
    def width(self, value):
        """Sets width attribute."""
        self.integer_validator("width", value)
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets height attribute."""
        self.integer_validator("height", value)
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets x attribute."""
        self.integer_validator("x", value)
        self.x_y_validator("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets y attribute."""
        self.integer_validator("y", value)
        self.x_y_validator("y", value)
        self.__y = value

    def area(self):
        """Computes the area  of Rectangle instance"""
        return (self.__width * self.__height)

    def display(self):
        for i in range(self.__height):
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y,
            self.__width, self.__height
        )
