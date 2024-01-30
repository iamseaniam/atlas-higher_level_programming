#!/usr/bin/python3
"""square Module"""

from .rectangle import Rectangle


class square(Rectangle):
    """Square class inheriting from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square class"""
        super().__init__(size, size, x, y, id)
        
    def __str__(self):
        """Override the __str__ method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    
    @property
    def size(self):
        """Getter for size"""
        return self.width
    
    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value
