#!/usr/bin/python3
"""Module 9-student"""


class Student:
    """class that defines a Student object.
    Args:
        - first_name
        - last_name
        - age
    """
    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to_json
        convert the instance of Student class to json.

        Returns: the dict representation of the instance.
        """
        res = self.__dict__
        return res
