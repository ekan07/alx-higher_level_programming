#!/usr/bin/python3


class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        """Unimplemented area function.
        Raise: if area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator
        Args
           name: name of value
           value: value
        Raise:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
