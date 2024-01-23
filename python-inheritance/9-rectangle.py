#!/usr/bin/python3
'''Rectangle module'''


class BaseGeometry:
    '''BaseGeometry class definition'''

    def area(self):
        '''Placeholder for area calculation'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validate integer values'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    '''Rectangle class definition'''

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Calculate the area of the rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''String representation of the rectangle'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


