#!/usr/bin/python3
"""Module 10-student.
Creates a Student class.
"""


class Student:
    """class that defines a Student object.
    Args:
        - first_name
        - last_name
        - age
    method to_json().
    method reload_from_json().
    """
    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation
        of a Student instance.
        Args:
            - attrs: list of attributes
        Returns: the dict representation of the instance.
        """
        my_dict = dict()
        if attrs and all(isinstance(i, str) for i in attrs):
            for i in attrs:
                if i in self.__dict__:
                    my_dict.update({i: self.__dict__[i]})
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.
        Args:
            - json: dictionnary of attributes
        """
        for i in json:
            self.__dict__.update({i: json[i]})
