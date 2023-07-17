import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """A class that tests the Base class"""

    def test_init(self):
        """Test the initialization of a Base instance"""

        # Create a Base instance with no id
        b1 = Base()

        # Check if the id is assigned correctly
        self.assertEqual(b1.id, 1)

        # Create another Base instance with no id
        b2 = Base()

        # Check if the id is incremented correctly
        self.assertEqual(b2.id, 2)

        # Create a Base instance with a given id
        b3 = Base(12)

        # Check if the id is assigned correctly
        self.assertEqual(b3.id, 12)

    def test_to_json_string(self):
        """Test the to_json_string static method of the Base class"""

        # Create a list of dictionaries
        list_dicts = [{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},
                      {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]

        # Call the to_json_string method and store the result
        json_string = Base.to_json_string(list_dicts)

        # Check if the result is a string
        self.assertIsInstance(json_string, str)

        # Check if the result matches the expected JSON string
        expected = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, ' \
                   '{"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
        self.assertEqual(json_string, expected)

    def test_save_to_file(self):
        """Test the save_to_file class method of the Base class"""

        # Create a list of Rectangle instances
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles = [r1, r2]

        # Call the save_to_file method with the list of rectangles
        Rectangle.save_to_file(list_rectangles)

        # Read the file and store its content as a string
        with open("Rectangle.json", "r") as f:
            data = f.read()

        # Check if the file content matches the expected JSON string
        expected = '[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, ' \
                   '{"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]'
        self.assertEqual(data ,expected)

    def test_from_json_string(self):
       """Test the from_json_string static method of the Base class"""

       # Create a JSON string representation of a list of dictionaries
       json_string = '[{"id":89 ,"width":10 ,"height":4 ,"x":7 ,"y":8} ,{"id":7 ,"width":1 ,"height":7 ,"x":8 ,"y":4}]'

       # Call the from_json_string method and store the result
       list_dicts = Base.from_json_string(json_string)

       # Check if the result is a list
       self.assertIsInstance(list_dicts ,list)

       # Check if the result matches the expected list of dictionaries
       expected = [{"id" :89 ,"width" :10 ,"height" :4 ,"x" :7 ,"y" :8} ,{"id" :7 ,"width" :1 ,"height" :7 ,"x" :8 ,"y" :4}]
       self.assertListEqual(list_dicts ,expected)

    def test_create(self):
       """Test the create class method of the Base class"""

       # Create a dictionary of attributes for a Rectangle instance
       r_dict = {"id" :89 ,"width" :10 ,"height" :4 ,"x" :7 ,"y" :8}

       # Call the create method and store the result
       r1 = Rectangle.create(**r_dict)

       # Check if the result is an instance of Rectangle
       self.assertIsInstance(r1 ,Rectangle)

       # Check if the result has the correct attributes
       self.assertEqual(r1.id ,89)
       self.assertEqual(r1.width ,10)
       self.assertEqual(r1.height ,4)
       self.assertEqual(r1.x ,7)
       self.assertEqual(r1.y ,8)

    def test_load_from_file(self):
       """Test the load_from_file class method of the Base class"""

       # Create a list of Rectangle instances
       r1 = Rectangle(10, 7, 2, 8)
       r2 = Rectangle(2, 4)
       list_rectangles = [r1, r2]

       # Call the save_to_file method with the list of rectangles
       Rectangle.save_to_file(list_rectangles)

       # Call the load_from_file method and store the result
       list_rectangles_output = Rectangle.load_from_file()

       # Check if the result is a list
       self.assertIsInstance(list_rectangles_output ,list)

       # Check if the result matches the expected list of instances
       self.assertEqual(str(list_rectangles_output[0]) ,"[Rectangle] (1) 2/8 - 10/7")
       self.assertEqual(str(list_rectangles_output[1]) ,"[Rectangle] (2) 0/0 - 2/4")

    def test_save_to_file_csv(self):
        """Test the save_to_file_csv class method of the Base class"""

        # Create a list of Square instances
        s1 = Square(10, 5, 6, 1)
        s2 = Square(20, 7, 8, 2)
        list_squares = [s1, s2]

        # Call the save_to_file_csv method with the list of squares
        Square.save_to_file_csv(list_squares)

        # Read the file and store its content as a string
        with open("Square.csv", "r") as f:
            data = f.read()

        # Check if the file content matches the expected CSV string
        expected = "1,10,5,6\n2,20,7,8\n"
        self.assertEqual(data ,expected)

    def test_draw(self):
        """Test the draw method of the Base class"""

        # Create a list of Rectangle instances
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles = [r1, r2]

        # Create a list of Square instances
        s1 = Square(10, 5, 6)
        s2 = Square(20, 7, 8)
        list_squares = [s1, s2]

        # Call the draw method with the lists of rectangles and squares
        Base.draw(list_rectangles, list_squares)

        # Check if the turtle graphics window is displayed
        self.assertTrue(turtle.Screen()._isopen)

if __name__ == "__main__":
    unittest.main()

