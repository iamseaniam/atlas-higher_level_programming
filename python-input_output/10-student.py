#!/usr/bin/python3
"""documentatin for all the stuff"""


class Student:
    """documentatin for all the stuff"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        student_dict = {}
        if attrs is None or not isinstance(attrs, list):
            attrs = list(self.__dict__.keys())
        for key in attrs:
            if key in self.__dict__ and hasattr(self.__dict__[key], '__dict__'):
                student_dict[key] = class_to_json(self.__dict__[key])
            elif key in self.__dict__:
                student_dict[key] = self.__dict__[key]
        return student_dict
