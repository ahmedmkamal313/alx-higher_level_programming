#!/usr/bin/python3


import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """A class that tests the Rectangle class"""

    def test_init(self):
        """Test the initialization of a Rectangle instance"""

        # Create a Rectangle instance with valid arguments
        r1 = Rectangle(10, 20, 5, 6, 1)

        # Check if the attributes are assigned correctly
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 6)
        self.assertEqual(r1.id, 1)

    def test_area(self):
        """Test the area method of a Rectangle instance"""

        # Create a Rectangle instance with valid arguments
        r1 = Rectangle(10, 20, 5, 6, 1)

        # Check if the area method returns the correct value
        self.assertEqual(r1.area(), 200)

    def test_display(self):
        """Test the display method of a Rectangle instance"""

        # Create a Rectangle instance with valid arguments
        r1 = Rectangle(3, 2, 2, 2, 1)

        # Capture the output of the display method using StringIO
        from io import StringIO
        import sys
        output = StringIO()
        sys.stdout = output

        # Call the display method
        r1.display()

        # Restore the original stdout
        sys.stdout = sys.__stdout__

        # Check if the output matches the expected string
        expected = "\n\n  ###\n  ###\n"
        self.assertEqual(output.getvalue(), expected)

    def test_str(self):
        """Test the __str__ method of a Rectangle instance"""

        # Create a Rectangle instance with valid arguments
        r1 = Rectangle(3, 2, 2, 2, 1)

        # Check if the __str__ method returns the correct string
        expected = "[Rectangle] (1) 2/2 - 3/2"
        self.assertEqual(str(r1), expected)

    def test_update(self):
        """Test the update method of a Rectangle instance"""

        # Create a Rectangle instance with valid arguments
        r1 = Rectangle(10, 20, 5, 6, 1)

        # Call the update method with positional arguments
        r1.update(2, 30, 40, 7, 8)

        # Check if the attributes are updated correctly
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 30)
        self.assertEqual(r1.height, 40)
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.y, 8)

        # Call the update method with keyword arguments
        r1.update(x=9, height=50, y=10, width=60)

        # Check if the attributes are updated correctly
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 60)
        self.assertEqual(r1.height, 50)
        self.assertEqual(r1.x, 9)
        self.assertEqual(r1.y, 10)

    def test_to_dictionary(self):
       """Test the to_dictionary method of a Rectangle instance"""

       # Create a Rectangle instance with valid arguments
       r1 = Rectangle(10,20 ,5 ,6 ,1)

       # Call the to_dictionary method and store the result
       r_dict = r1.to_dictionary()

       # Check if the result is a dictionary with the correct key-value pairs
       self.assertIsInstance(r_dict ,dict)
       self.assertDictEqual(r_dict ,{"x":5 ,"y":6 ,"id":1 ,"height":20 ,"width":10})

if __name__ == "__main__":
    unittest.main()
