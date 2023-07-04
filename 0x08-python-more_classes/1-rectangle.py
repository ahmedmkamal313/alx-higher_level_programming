#!/usr/bin/python3

"""Defines a rectangle class"""


class Rectangle:
    """Defines a Rectangle class with private attributes"""

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height
        Args:
            width : The width of the rectangle.
            height: The height of the rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
