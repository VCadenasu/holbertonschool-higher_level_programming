#!/usr/bin/python3
"""define a rectangle"""


class Rectangle:
    """Sets the rectangle"""
    def __init__(self, height=0, width=0):
        """Args:
            width (int): sets the width of the rectangle.
            height (int): sets the height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Sets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not (value, int):
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
        if not (value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
