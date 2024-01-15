"""
This is a module for demonstrating classes in Python.
"""


class Square:
    """
    This class represents a square. It has a private attribute '__size' which represents the size of the square.
    The size of the square is set during instantiation and cannot be changed afterwards.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
