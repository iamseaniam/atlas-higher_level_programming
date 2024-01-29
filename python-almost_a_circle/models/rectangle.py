#!/usr/bin/python3
"""Rectangle module"""


from .base import Base


class Rectangle(Base):
    """Rectangle class inheriting from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for Rectangle class"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for Width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for Width"""
        self.validate_integer(value, "width")
        self.validate_positive(value, "width")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for Height"""
        self.validate_integer(value, "height")
        self.validate_positive(value, "height")
        self.__height = value

    @property
    def x(self):
        """Getter for X"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for X"""
        self.validate_integer(value, "x")
        self.validate_positive(value, "x")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for Y"""
        self.validate_integer(value, "y")
        self.validate_positive(value, "y")
        self.__y = value
