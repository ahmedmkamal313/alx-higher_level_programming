# 0x0A-python-inheritance

This project is about learning the basics of inheritance in Python, a key concept of object-oriented programming.

### Concepts:
- inheritance
- multiple inheritance
- superclass
- subclass

### Requirements:
- **Python Scripts:**
  - Allowed editors: `vi`, `vim`, `emacs`
  - All the files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
  - The first line of all the files should be exactly `#!/usr/bin/python3`
  - The code should use the pycodestyle (version `2.8.*`)
  - All the files must be executable
  - The length of the files will be tested using `wc`

### List of contents:
- **0-lookup.py:**
	- a function that returns the list of available attributes and methods of an object
	- Prototype: `def lookup(obj):`
- **1-my_list.py:**
 	- a class MyList that inherits from list.
	- Public instance method: `def print_sorted(self)`: that prints the list, but sorted (ascending sort)
- **2-is_same_class.py**
	- a function that returns `True` if the object is exactly an instance of the specified class ; otherwise `False`
	- Prototype: `def is_same_class(obj, a_class):`
- **3-is_kind_of_class.py:**
	- a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`
	- Prototype: `def is_kind_of_class(obj, a_class):`
- **4-inherits_from.py:**
	- a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.
	- Prototype: `def inherits_from(obj, a_class):`
- **5-base_geometry.py:**
	- an empty class `BaseGeometry`.
- **6-base_geometry.py:**
	- a class `BaseGeometry` (based on `5-base_geometry.py`).
	- Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
- **7-base_geometry.py:**
	- a class `BaseGeometry` (based on `6-base_geometry.py`).
	- Public instance method: `def area(self):` that raises an Exception with the message `area() is not implemented`
	- Public instance method: `def integer_validator(self, name, value):` that validates `value`
- **8-rectangle.py:**
	- a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`).
	- Instantiation with width and height: `def __init__(self, width, height):`
- **9-rectangle.py:**
	- a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`). (task based on `8-rectangle.py`)
	- Instantiation with width and height: `def __init__(self, width, height):`
- **10-square.py:**
	- a class `Square` that inherits from `Rectangle` (`9-rectangle.py`):
	- Instantiation with size: `def __init__(self, size):`
- **11-square.py:**
	- a class `Square` that inherits from `Rectangle` (`9-rectangle.py`). (task based on `10-square.py`).
	- Instantiation with size: `def __init__(self, size):`
- **100-my_int.py:**
	- a class `MyInt` that inherits from `int`
	- `MyInt` is a rebel. `MyInt` has `==` and `!=` operators inverted
- **101-add_attribute.py:**
	- a function that adds a new attribute to an object if it’s possible.
	- Prototype: `def add_attribute(obj, name, value)`

- **tests:**
    > this directory contain all the test files.
    - 1-my_list.txt
    - 7-base_geometry.txt
