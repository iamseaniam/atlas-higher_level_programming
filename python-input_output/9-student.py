#!/usr/bin/python3
"""documentatin for all the stuff"""


class Student:
    """documentatin for all the stuff"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """documentatin for all the stuff"""
        student_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                student_dict[key] = value
            elif hasattr(value, '__dict__'):
                student_dict[key] = class_to_json(value)
        return student_dict
