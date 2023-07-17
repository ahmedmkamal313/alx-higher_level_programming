# 0x0C. Python - Almost a circle

This project is a review of everything about Python, including:
- Import
- Exceptions
- Class
- Private attribute
- Getter/Setter
- Class method
- Static method
- Inheritance
- Unittest
- Read/Write file
It also covers some new topics, such as:
- args and kwargs
- Serialization/Deserialization
- JSON

## Requirements
- Python 3.7 or higher
- PEP 8 style

| **File** 			      | **Description** 				 |
| :--- 				      |	 					    ---: |
| models/base.py                      | The base class for all other classes             |
| models/init.py                      | An empty file that makes models a Python package |
| models/rectangle.py                 | The class Rectangle that inherits from Base      |
| models/square.py                    | The class Square that inherits from Rectangle    |
| tests/test_models/test_base.py      | The unittests for the base class                 |
| tests/test_models/test_rectangle.py | The unittests for the rectangle class            |
| tests/test_models/test_square.py    | The unittests for the square class               |

### Usage:

To use the classes, you can import them from the models package:
```
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
```
To run the unittests, you can use the following command:
```
python3 -m unittest discover tests
```
To create an instance of a class, you can use the constructor with the appropriate arguments:
```
r1 = Rectangle(10, 2)
s1 = Square(5)
```
To access or modify the attributes of an instance, you can use getters and setters or dot notation:
```
r1.width # getter
r1.width = 12 # setter
r1.x # dot notation
r1.x = 3 # dot notation
```
To call a class or static method, you can use the class name or an instance:
```
Rectangle.to_json_string([r1.to_dictionary()]) # class method
r1.area() # instance method
Square.validate_size(7) # static method
s1.display() # instance method
```
To serialize or deserialize an instance, you can use the methods from_json_string and create:
```
json_string = Rectangle.to_json_string([r1.to_dictionary()])
list_of_dictionaries = Rectangle.from_json_string(json_string)
r2 = Rectangle.create(**list_of_dictionaries[0])
```
To write or read a JSON file, you can use the methods save_to_file and load_from_file:
```
Rectangle.save_to_file([r1, r2])
list_of_rectangles = Rectangle.load_from_file()
```
