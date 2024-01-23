#!/usr/bin/python3
'''this is how you document'''


class Rectangle(BaseGeometry):
    '''this is how you document'''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
