#!/usr/bin/python3

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """A class that tests the Square class"""

    def test_init(self):
        """Test the initialization of a Square instance"""

        # Create a Square instance with valid arguments
        s1 = Square(10, 5, 6, 1)

        # Check if the attributes are assigned correctly
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 6)
        self.assertEqual(s1.id, 1)

    def test_str(self):
        """Test the __str__ method of a Square instance"""

        # Create a Square instance with valid arguments
        s1 = Square(10, 5, 6, 1)

        # Check if the __str__ method returns the correct string
        expected = "[Square] (1) 5/6 - 10"
        self.assertEqual(str(s1), expected)

    def test_update(self):
        """Test the update method of a Square instance"""

        # Create a Square instance with valid arguments
        s1 = Square(10, 5, 6, 1)

        # Call the update method with positional arguments
        s1.update(2, 20, 7, 8)

        # Check if the attributes are updated correctly
        self.assertEqual(s1.id, 2)
        self.assertEqual(s1.size, 20)
        self.assertEqual(s1.x, 7)
        self.assertEqual(s1.y, 8)

        # Call the update method with keyword arguments
        s1.update(x=9, size=30, y=10)

        # Check if the attributes are updated correctly
        self.assertEqual(s1.id, 2)
        self.assertEqual(s1.size, 30)
        self.assertEqual(s1.x, 9)
        self.assertEqual(s1.y, 10)

    def test_to_dictionary(self):
       """Test the to_dictionary method of a Square instance"""

       # Create a Square instance with valid arguments
       s1 = Square(10 ,5 ,6 ,1)

       # Call the to_dictionary method and store the result
       s_dict = s1.to_dictionary()

       # Check if the result is a dictionary with the correct key-value pairs
       self.assertIsInstance(s_dict ,dict)
       self.assertDictEqual(s_dict ,{"x":5 ,"y":6 ,"id":1 ,"size":10})

if __name__ == "__main__":
    unittest.main()
