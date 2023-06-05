# **0x00. Python - Hello, World**

- ### **Requirements:**
  - **Python Scripts:**
    - Allowed editors: vi, vim, emacs.
    - files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
    - code should use the pycodestyle (version 2.8.*).
    - The first line of all files should be exactly **#!/usr/bin/python3**
    - length of files will be tested using wc.
  - **Shell Scripts:**
    - Allowed editors: vi, vim, emacs
    - All scripts will be tested on Ubuntu 20.04 LTS
    - All scripts should be exactly two lines long (wc -l file should print 2)
    - All files should end with a new line
    - The first line of all files should be exactly **#!/bin/bash**
    - All files must be executable

Included files:

- **0-run:**
  - a Shell script that runs a Python script.
  - The Python file name will be saved in the environment variable $PYFILE.
  
- **1-run_inline:**
  - a Shell script that runs Python code.
  - The Python code will be saved in the environment variable $PYCODE.
  
- **2-print.py:**
  - Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.
    - Use the function print.

- **3-print_number.py:**
  - Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.
    ``` 
      #!/usr/bin/python3
      number = 98
      #YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
      ```
  - The output of the script should be:
    - the number, followed by Battery street,
    - followed by a new line.
  - not allowed to cast the variable number into a string.
  - code must be 3 lines long.
  - use f-strings tips.
  
- **4-print_float.py:**
  - Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.
    ```
     #!/usr/bin/python3
     number = 3.14159
     #YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE.
     ```
  - The output of the program should be:
    - Float:, followed by the float with only 2 digits
    - followed by a new line.
  - not allowed to cast number to string.
  - use f-strings.

- **5-print_string.py:**
  - Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.
    ```
     #!/usr/bin/python3
     str = "Holberton School"
     #YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
     ```
  - The output of the program should be:
    - 3 times the value of str.
    - followed by a new line.
    - followed by the 9 first characters of str.
    - followed by a new line.
  - not allowed to use any loops or conditional statement.
  - program should be maximum 5 lines long.

- **6-concat.py:**
  - print Welcome to Holberton School!
    - not allowed to use any loops or conditional statements.
    - have to use the variables str1 and str2 in your new line of code.
    - program should be exactly 5 lines long.

- **7-edges.py:**
  - Complete this source code:
    ```  
    #!/usr/bin/python3
    word = "Holberton"
    #YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
    print(f"First 3 letters: {word_first_3}")
    print(f"Last 2 letters: {word_last_2}")
    print(f"Middle word: {middle_word}")
    ```
  - not allowed to use any loops or conditional statements.
  - program should be exactly 8 lines long.
  - word_first_3 should contain the first 3 letters of the variable word.
  - word_last_2 should contain the last 2 letters of the variable word.
  - middle_word should contain the value of the variable word without the first and last letters.

- **8-concat_edges.py:**
  - Complete this source code to print object-oriented programming with Python, followed by a new line.
    ```
     #!/usr/bin/python3
     str = "Python is an interpreted, interactive, object-oriented programming\
     language that combines remarkable power with very clear syntax"
     #YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
     print(str)
    ```
  - not allowed to use any loops or conditional statements.
  - program should be exactly 5 lines long.
  - not allowed to create new variables.
  - not allowed to use string literals.

- **9-easter_egg.py:**
  - Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.
    - script should be maximum 98 characters long.
    - check with `wc -m 9-easter_egg.py`

- **10-check_cycle.c:**
  - Write a function in C that checks if a singly linked list has a cycle in it.
    - Prototype: int check_cycle(listint_t *list);
    - Return: 0 if there is no cycle, 1 if there is a cycle
    > Solving a problem is already a big win! but finding the best and optimal way to solve it, it’s way better! Think about the most optimal / fastest way to do it.

- **100-write.py:**
  - a Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.
    - Use the function write from the `sys` module.
    - not allowed to use `print`.
    - script should print to `stderr`.
    - script should exit with the status code `1`.
