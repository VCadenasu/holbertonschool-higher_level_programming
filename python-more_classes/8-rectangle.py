#!/usr/bin/python3
"""define a rectangle"""


class Rectangle:
    """Sets the rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Args:
            width (int): sets the width of the rectangle.
            height (int): sets the height of the rectangle.
        """
        type(self).number_of_instances += 1
        self.height = height
        self. width = width

    @property
    def width(self):
        """Sets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """sets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return (0)
        else:
            return (2 * self.width) + (2 * self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns a rectangle with greater area.

        Args:
            rect_1 (rectangle): first one
            rect_2 (rectangle): second one
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ("")
        rect = []
        for i in range(self.height):
            [rect.append(str(self.print_symbol)) for j in range(self.width)]
            if i != self.height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        rect = "Rectangle(" + str(self.width)
        rect += ", " + str(self.height) + ")"
        return (rect)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
