# 0x03. Python - Data Structures: Lists, Tuples
  ![python is fun](https://th.bing.com/th/id/OIP.Uc0oC3OLG1Trulc0j-jBCQAAAA?pid=ImgDet&rs=1)
## Requirements

**Python Scripts**
  - Allowed editors: `vi`, `vim`, `emacs`.
  - All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
  - All files should end with a new line.
  - The first line of all files should be exactly `#!/usr/bin/python3`.
  - A `README.md` file, at the root of the folder of the project, is mandatory.
  - the code should use the pycodestyle (version `2.8.*`).
  - All files must be executable.
  - The length of the files will be tested using `wc`.

**C**
  - Allowed editors: `vi`, `vim`, `emacs`.
  - All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
  - All files should end with a new line.
  - code should use the `Betty` style. It will be checked using betty-style.pl and betty-doc.pl.
  - not allowed to use global variables.
  - No more than 5 functions per file.
  - In the following examples, the `main.c` files are shown as examples.
  - The prototypes of all functions should be included in a header file called `lists.h`.
  - All the header files should be include guarded.

## List of files

- **0-print_list_integer.py:**
  - a function that prints all integers of a list.
    - Prototype: `def print_list_integer(my_list=[]):`
    - `str.format()` to print integers.
    - Format: one integer per line. See example:
  ```
  /0x03-python-data_structures$ ./0-main.py
  1
  2
  3
  4
  5
  ```

- **1-element_at.py:**
  - a function that retrieves an element from a list like in C.
    - Prototype: `def element_at(my_list, idx):`
    - If `idx` is negative, the function should return `None`.
    - If `idx` is out of range (> of number of element in `my_list`), the function should return `None`.

- **2-replace_in_list.py:**
  - a function that replaces an element of a list at a specific position (like in C).
    - Prototype: `def replace_in_list(my_list, idx, element):`
    - If `idx` is negative, the function should not modify anything, and returns the original `list`.
    - If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original `list`.

- **3-print_reversed_list_integer.py:**
  - a function that prints all integers of a list, in reverse order.
    - Prototype: `def print_reversed_list_integer(my_list=[]):`.
    - str.format() to print integers.
    - Format: one integer per line. See example:
  ```
  /0x03-python-data_structures$ ./3-main.py
  5
  4
  3
  2
  1
  ```

- **4-new_in_list.py:**
  - a function that replaces an element in a list at a specific position without modifying the original list (like in C).
    - Prototype: `def new_in_list(my_list, idx, element):`
    - If `idx` is negative, the function should return a copy of the original list.
    - If `idx` is out of range (> of number of element in `my_list`), the function should return a copy of the original list.

- **5-no_c.py:**
  - Write a function that removes all characters `c` and `C` from a string.
    - Prototype: `def no_c(my_string):`.
    - The function should return the new string.

- **6-print_matrix_integer.py:**
  - a function that prints a matrix of integers.
    - Prototype: `def print_matrix_integer(matrix=[[]]):`.
    - str.format() to print integers.
    - Format: see example
  ```
  /0x03-python-data_structures$ ./6-main.py | cat -e
  1 2 3$
  4 5 6$
  7 8 9$
  --$
  $
  /0x03-python-data_structures$
  ```

- **7-add_tuple.py:**
  - a function that adds 2 tuples.
    - Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
    - Returns a tuple with 2 integers:
      - The first element should be the addition of the first element of each argument.
      -	The second element should be the addition of the second element of each argument.
    - If a tuple is smaller than 2, use the value `0` for each missing integer.
    - If a tuple is bigger than 2, use only the first 2 integers.

- **8-multiple_returns.py:**
  - a function that returns a tuple with the length of a string and its first character.
  - Prototype: `def multiple_returns(sentence):`
  - If the sentence is empty, the first character should be equal to `None`.

- **9-max_integer.py:**
  - a function that finds the biggest integer of a list.
  - Prototype: `def max_integer(my_list=[]):`.
  - If the list is empty, return `None`.

- **10-divisible_by_2.py:**
  - a function that finds all multiples of 2 in a list.
  - Prototype: `def divisible_by_2(my_list=[]):`.
  - Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2.
  - The new list should have the same size as the original list.

- **11-delete_at.py:**
  - a function that deletes the item at a specific position in a list.
  - Prototype: def `delete_at(my_list=[], idx=0):`.
  - If idx is negative or out of range, nothing change (returns the same list).

