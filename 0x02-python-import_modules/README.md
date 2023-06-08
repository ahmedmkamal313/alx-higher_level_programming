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
