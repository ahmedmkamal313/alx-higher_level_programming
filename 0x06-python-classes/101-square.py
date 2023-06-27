#!/usr/bin/python3

class Square:
    """A class that defines a square by size and position"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with optional size and position

        Args:
            size (int, optional): length of the side of square. Defaults to 0.
            position (tuple, optional): The coordinates of the
            bottom-left corner of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square

        Returns:
            int: The length of the side of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square

        Args:
            value (int): The new length of the side of the square

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is negative
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #

        If size is equal to 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    def __str__(self):
        """Return a string representation of the square

        The square is represented by the '#' character.

        Returns:
            str: The string representation of the square.
        """
        output = ""
        if self.__size == 0:
            output += "\n"
            return output
        for i in range(self.__position[1]):
            output += "\n"
        for i in range(self.__size):
            output += " " * self.__position[0]
            output += "#" * self.__size
            if i < self.__size - 1:
                output += "\n"
        return output
