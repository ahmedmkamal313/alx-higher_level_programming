#!/usr/bin/python3
"""Test cases for the Base class"""

import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """A class to test the Base class"""

    def setUp(self):
        """Reset the number of objects before each test"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test the id attribute of the Base class"""

        # Test if id is assigned correctly when given
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

        # Test if id is incremented correctly when not given
        b2 = Base()
        self.assertEqual(b2.id, 1)

        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_to_json_string(self):
        """Test the to_json_string static method of the Base class"""

        # Test if the method returns "[]" when given None or an empty list
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

        # Test if the method returns the correct JSON string representation
        # of a list of dictionaries
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), str)
        self.assertDictEqual(dictionary, json.loads(json_dictionary)[0])

    def test_save_to_file(self):
        """Test the save_to_file class method of the Base class"""

        # Test if the method creates an empty file when given None or an empty list
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        Base.save_to_file([])
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        # Test if the method writes the correct JSON string representation
        # of a list of objects to a file
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            data = f.read()
            list_dict = json.loads(data)
            self.assertEqual(type(list_dict), list)
            self.assertDictEqual(list_dict[0], r1.to_dictionary())
            self.assertDictEqual(list_dict[1], r2.to_dictionary())

    def test_from_json_string(self):
        """Test the from_json_string static method of the Base class"""

        # Test if the method returns an empty list when given None or an empty string
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        # Test if the method returns the correct list of dictionaries from a JSON string
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
            ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)
        self.assertDictEqual(list_output[0], list_input[0])
        self.assertDictEqual(list_output[1], list_input[1])

    def test_create(self):
        """Test the create class method of the Base class"""

        # Test if the method returns an instance with all attributes already set
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
