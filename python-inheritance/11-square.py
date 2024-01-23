#!/usr/bin/python3
'''Square module'''

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

class Square(Rectangle):
    '''Square class definition'''

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        '''String representation of the square'''
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
