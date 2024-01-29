#!/usr/bin/python3\
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

        def width(self):
            """Getter for Width"""
            return self.__width
        
        def width(self, value):
            """Setter for Width"""
            self.__width = value
            
        def height(self):
            """Getter for height"""
            return self.__height
        
        def height (self, value):
            """setter for Height"""
            self.__height = value
            
        def x(self):
            """getter for X"""
            return self.x
        
        def x(self, value):
            """Setter for X"""
            self.__x = value
    
        def y(self):
            """getter for y"""
            return self.__y
        
        def y(self, value):
            """Setter for Y"""
            self.__y = value       
        
            
        