#!/usr/bin/python3
"""
This is a module for demonstrating classes in Python.
"""


class Square:
    """
    This class represents a square. It has a private attribute '__size'.
    The size of the square is set during instantiation and cannot be cha.
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2
