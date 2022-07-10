#!/usr/bin/python3
"""Module 10-student.
"""


class Student:
    """class that defines a Student object.
    Args:
        - first_name
        - last_name
        - age
    Method to_json().
    """
    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json

        Returns: the dict representation of the instance.
        """
        my_dict = dict()
        if type(attrs) is list and all(type(i) is str for i in attrs):
            for i in attrs:
                if i in self.__dict__:
                    my_dict.update({i: self.__dict__[i]})
            return my_dict
        return self.__dict__.copy()
