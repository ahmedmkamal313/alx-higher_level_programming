#!/usr/bin/python3
"""Defines a base model class."""


import json


class Base:
    """A base class for other classes in the project"""

    # a private class attribute to keep track of number of objects
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance with an optional id"""

        # If id is given, assign it to the public instance attribute id
        if id is not None:
            self.id = id
        # otherwise increment the class attribute and assign it to the id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""

        # If list_dictionaries is None or empty, return the string "[]"
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        # Otherwise, use the json.dumps method to return
        # the JSON string representation of list_dictionaries
        return json.dumps(list_dictionaries)
