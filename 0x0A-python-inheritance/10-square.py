#!/usr/bin/python3
"""a class Square that inherits from Rectangle"""


# Import Rectangle from 9-rectangle.py module
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """A class that represents a square"""

    def __init__(self, size):
        """Initializes a square with size"""
        # Validate size as a positive integer
        self.integer_validator("size", size)
        # assign size as a private attribute
        self.__size = size
        # call the parent class constructor with width and height equal to size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
