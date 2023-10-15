#!/usr/bin/python3
"""define a rectangle"""


class Rectangle:
    """Sets the rectangle"""
    def __init__(self, width=0, height=0):
        """Args:
            width (int): sets the width of the rectangle.
            height (int): sets the height of the rectangle.
        """
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

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ("")
        rect = []
        for i in range(self.height):
            [rect.append("#") for j in range(self.width)]
            if i != self.height - 1:
                rect.append("\n")
        return ("".join(rect))
