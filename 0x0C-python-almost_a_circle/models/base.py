#!/usr/bin/python3
"""Defines a base model class."""


class base:
    """A base class for other classes in the project"""

    # a private class attribute to keep track of number of objects
    _nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance with an optional id"""

        # If id is given, assign it to the public instance attribute id
        if id is not None:
            self.id = id
        # otherwise increment the class attribute and assign it to the id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
