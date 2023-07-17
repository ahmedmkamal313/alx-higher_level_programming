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
        # Test if r1 and r2 are different objects
        self.assertIsNot(r1, r2)

        # Test if r1 and r2 have the same attributes
        self.assertEqual(r1.id, r2.id)
        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)

    def test_load_from_file(self):
        """Test the load_from_file class method of the Base class"""

        # Test if the method returns an empty list when the file does not exist
        self.assertEqual(Base.load_from_file(), [])
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

        # Test if the method returns a list of instances from a file
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        # Test if the output list has the same length as the input list
        self.assertEqual(len(list_rectangles_output), len(list_rectangles_input))

        # Test if each element in the output list has the same attributes as
        # the corresponding element in the input list
        for i in range(len(list_rectangles_output)):
            self.assertEqual(list_rectangles_output[i].id,
                             list_rectangles_input[i].id)
            self.assertEqual(list_rectangles_output[i].width,
                             list_rectangles_input[i].width)
            self.assertEqual(list_rectangles_output[i].height,
                             list_rectangles_input[i].height)
            self.assertEqual(list_rectangles_output[i].x,
                             list_rectangles_input[i].x)
            self.assertEqual(list_rectangles_output[i].y,
                             list_rectangles_input[i].y)

    def test_save_to_file_csv(self):
        """Test the save_to_file_csv class method of the Base class"""

        # Test if the method writes the correct CSV representation
        # of a list of objects to a file
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])

    def test_load_from_file_csv(self):
        """Test the load_from_file_csv class method of the Base class"""

        # Test if the method returns an empty list when the file does not exist
        self.assertEqual(Base.load_from_file_csv(), [])
        self.assertEqual(Rectangle.load_from_file_csv(), [])
        self.assertEqual(Square.load_from_file_csv(), [])

        # Test if the method returns a list of instances from a CSV file
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file_csv(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file_csv()

        # Test if the output list has the same length as the input list
        self.assertEqual(len(list_rectangles_output), len(list_rectangles_input))

        # Test if each element in the output list has the same attributes as
        # the corresponding element in the input list
        for i in range(len(list_rectangles_output)):
            self.assertEqual(list_rectangles_output[i].id,
                             list_rectangles_input[i].id)
            self.assertEqual(list_rectangles_output[i].width,
                             list_rectangles_input[i].width)
            self.assertEqual(list_rectangles_output[i].height,
                             list_rectangles_input[i].height)
            self.assertEqual(list_rectangles_output[i].x,
                             list_rectangles_input[i].x)
            self.assertEqual(list_rectangles_output[i].y,
                             list_rectangles_input[i].y)
    def test_invalid_id(self):
        """Test passing an invalid id to the Base constructor"""

        # Test passing a negative id
        b1 = Base(-1)
        self.assertEqual(b1.id, -1)

        # Test passing a zero id
        b2 = Base(0)
        self.assertEqual(b2.id, 0)
