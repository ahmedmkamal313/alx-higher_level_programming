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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""

        list_dicts = [obj.to_dictionary() for obj in list_objs] \
            if list_objs else []

        # Use the to_json_string method to get
        # the JSON string representation of list_dicts
        json_string = cls.to_json_string(list_dicts)

        filename = cls.__name__ + ".json"

        with open(filename, "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""

        # If json_string is None or empty, return an empty list
        if json_string is None or not json_string:
            return []

        # Otherwise, use the json.loads method to
        # return the list represented by json_string
        return json.loads(json_string)
