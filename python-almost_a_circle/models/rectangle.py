#!/usr/bin/python3
"""Rectangle module"""

from .base import Base

class Rectangle(Base):
    """Rectangle class inheriting from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        self.validate_non_negative(value, "x")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for Y"""
        self.validate_integer(value, "y")
        self.validate_non_negative(value, "y")
        self.__y = value

    def validate_integer(self, value, attribute_name):
        """Validate if the value is an integer"""
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")

    def validate_positive(self, value, attribute_name):
        """Validate if the value is greater than 0"""
        if value <= 0:
            raise ValueError(f"{attribute_name} must be > 0")

    def validate_non_negative(self, value, attribute_name):
        """Validate if the value is greater than or equal to 0"""
        if value < 0:
            raise ValueError(f"{attribute_name} must be >= 0")
