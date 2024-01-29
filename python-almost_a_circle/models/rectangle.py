#!/usr/bin/python3\
"""Rectangle documentation"""


from .base import Base

class Rectangle(Base):
    """Rectangle documentation"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        
        def width(self):
            return self.__width
        
        def height(self):
            return self.__height

        def x(self):
            return self.__x

        def y(self):
            return self.__y
