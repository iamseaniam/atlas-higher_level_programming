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
        
        def set_width(self, value):
            self.__width = value

        def set_height(self, value):
            self.__height = value

        def set_x(self, value):
            self.__x = value

        def set_y(self, value):
            self.__y = value