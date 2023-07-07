# 0x07. Python - Test-driven development
This project is about learning how to use test-driven development (TDD) in Python. TDD is a software development process that involves writing tests before writing the actual code. This way, the code can be verified to meet the requirements and avoid bugs.

![test](https://lh6.googleusercontent.com/NW5kTmb-EH1HMYJ8reTqaf7NLI6K8HyZhQ1gGHCXTqObgzdAZQE0-2A4fTJAVp9YmTzMVWQmwkvEJr7aPpKg42UHJYdYXfrdy7dB82dH1NvveAJ1FXYkBGf-5FJEPF162ASnGSP8)

### Concepts:
- Never forget a test.
- Interactive and non-interactive tests.
- Unittest module.
- Doctest module.
- Docstrings.
### Requirements:
- Python 3.4 or higher.
- PEP 8 style.
- All files must be executable.

### List of content
- **0-add_integer.py:**
  - a function that adds 2 integers.
  - Prototype: `def add_integer(a, b=98):`
- **2-matrix_divided.py:**
  - a function that divides all elements of a matrix.
  - Prototype: `def matrix_divided(matrix, div):`
- **3-say_my_name.py:**
  - a function that prints `My name is <first name> <last name>`
  - Prototype: `def say_my_name(first_name, last_name=""):`
- **4-print_square.py:**
  - a function that prints a square with the character `#`.
  - Prototype: `def print_square(size):`
- **5-text_indentation.py:**
  - a function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`
  - Prototype: `def text_indentation(text):`
- **100-matrix_mul.py:**
  - a function that multiplies 2 matrices.
  - Prototype: `def matrix_mul(m_a, m_b):`
- **101-lazy_matrix_mul.py:**
  - a function that multiplies 2 matrices by using the module [NumPy](https://numpy.org/)
    - To install it: `pip3 install numpy==1.15.0`
  - Prototype: `def lazy_matrix_mul(m_a, m_b):`
- **102-python.c:**
  - a function that prints Python strings.
  - Prototype: `void print_python_string(PyObject *p);`
- **tests:**
  >this directory contain all the test files.
  - 0-add_integer.txt
  - 2-matrix_divided.txt
  - 3-say_my_name.txt
  - 4-print_square.txt
  - 5-text_indentation.txt
  - 6-max_integer_test.py
  - 100-matrix_mul.txt
  - 101-lazy_matrix_mul.txt
