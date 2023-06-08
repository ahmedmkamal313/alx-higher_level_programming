# 0x02. Python - import & modules
this project is a part of higher level programming from ALX SE.

**Requirements**

- General
  - Allowed editors: `vi, vim, emacs`
  - All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
  - All your files should end with a new line
  - The first line of all your files should be exactly `#!/usr/bin/python3`
  - A README.md file, at the root of the folder of the project, is mandatory
  - Your code should use the pycodestyle (version `2.8.*`)
  - All your files must be executable
  - The length of your files will be tested using `wc`

- **0-add.py:**
a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`
  - assign:
    - the value 1 to a variable called `a`
    - the value 2 to a variable called `b`
    - and use those two variables as arguments when calling the functions add and print
  - a and b must be defined in 2 different lines: `a = 1` and another `b = 2`

- **1-calculation.py:**
a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result.
  - define:
    - the value 10 to a variable `a`
    - the value 5 to a variable `b`
    - and use those two variables only, as arguments when calling functions (including print)
  - a and b must be defined in 2 different lines: `a = 10` and another `b = 5`

- **2-args.py:**
a program that prints the number of and the list of its arguments.
  - The output should be:
    - Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
      - : (or . if no arguments were passed) followed by
      - a new line, followed by (if at least one argument),
      - one line per argument:
        - the position of the argument (starting at `1`) followed by `:`, followed by the argument value and a new line
  - The number of elements of argv can be retrieved by using: `len(argv)`

- **3-infinite_add.py:**
a program that prints the result of the addition of all arguments.
  - The output should be the result of the addition of all arguments, followed by a new line.
  - cast arguments into integers by using `int()`
  - code should not be executed when imported
  - ![shocked to handle addition of big numbers](https://th.bing.com/th/id/OIP.C_v1yRhmotHXYW5IViBscQHaFH?pid=ImgDet&w=616&h=425&rs=1)

- **4-hidden_discovery.py:**
a program that prints all the names defined by the compiled module [hidden_4.pyc](https://github.com/alx-tools/0x02.py/raw/master/hidden_4.pyc).
  - one name per line, in alpha order.
  - print only names that do **not** start with `__`.
  - code should not be executed when imported.
  - Python3.8.x (`hidden_4.pyc` has been compiled with this version)

- **5-variable_load.py:**
 a program that imports the variable `a` from the file `variable_load_5.py` and prints its value.
  - should not be executed when imported.

- **100-my_calculator.py:**
a program that imports all functions from the `file calculator_1.py` and handles basic operations.
  - Usage: `./100-my_calculator.py a operator b`
    - If the number of arguments is not 3, your program has to:
      - print Usage: `./100-my_calculator.py <a> <operator> <b>` followed with a new line
      - exit with the value `1`
    - `operator` can be:
      - `+` for addition
      - `-` for subtraction
      - `*` for multiplication
      - `/` for division
    - If the `operator` is not one of the above:
      - print `Unknown operator. Available operators: +, -, * and /` followed with a new line
      - exit with the value `1`.
    - cast `a` and `b` into integers by using `int()`
    - The result should be printed like this: `<a> <operator> <b> = <result>`, followed by a new line.
  - code should not be executed when imported.

- **101-easy_print.py:**
a program that prints `#pythoniscool`, followed by a new line, in the standard output.
  - program should be maximum 2 lines long.
  - not allowed to use `print` or `eval` or `open` or `import sys` in  file `101-easy_print.py`
