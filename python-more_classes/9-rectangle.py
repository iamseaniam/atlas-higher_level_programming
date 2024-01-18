#!/usr/bin/python3
"""
documentation
"""


class Rectangle:
    """
    idk what to doc with this one
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 0 if self.width == 0 or self.height == 0 else 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return "\n".join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        return rect_1 if area_1 >= area_2 else rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    my_rectangle2 = Rectangle(3, 5)
    
    bigger_rect = Rectangle.bigger_or_equal(my_rectangle, my_rectangle2)
    
    print("Area of bigger rectangle: {}".format(bigger_rect.area()))
    print("Number of instances: {}".format(Rectangle.number_of_instances))

    square_instance = Rectangle.square(4)
    print("Square instance: {}".format(square_instance))
    print("Number of instances: {}".format(Rectangle.number_of_instances))

    del my_rectangle
    del my_rectangle2
    del square_instance
    print("Number of instances: {}".format(Rectangle.number_of_instances))