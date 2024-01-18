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

if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
    print("Number of instances: {}".format(Rectangle.number_of_instances))
    print(my_rectangle)

    Rectangle.print_symbol = "$"
    my_rectangle2 = Rectangle(3, 5)
    print("Area: {} - Perimeter: {}".format(my_rectangle2.area(), my_rectangle2.perimeter()))
    print("Number of instances: {}".format(Rectangle.number_of_instances))
    print(my_rectangle2)

    del my_rectangle
    print("Number of instances: {}".format(Rectangle.number_of_instances))

    del my_rectangle2
    print("Number of instances: {}".format(Rectangle.number_of_instances))
    