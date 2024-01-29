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
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for Height"""
        self.__height = value

    @property
    def x(self):
        """Getter for X"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for X"""
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for Y"""
        self.__y = value
