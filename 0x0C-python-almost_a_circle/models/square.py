#!/usr/bin/python3
"""Defines a square class."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance with the given attributes"""

        # Call the super class
        super().__init__(size, size, x, y, id)

        def __str__(self):
            """Returns a string representation of the Square instance"""

            return ("[Square] ({}) {}/{} - {}"
                    .format(self.id, self.x, self.y, self.width))
