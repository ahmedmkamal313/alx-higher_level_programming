# 0x04. Python - More Data Structures: Set, Dictionary

## Requirements:

**General:**
  - Allowed editors: `vi`, `vim`, `emacs`.
  - All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
  - All files should end with a new line.
  - The first line of all your files should be exactly `#!/usr/bin/python3`.
  - A `README.md` file, at the root of the folder of the project, is mandatory.
  - Your code should use the pycodestyle (version `2.8.*`).
  - All files must be executable.
  - The length of your files will be tested using `wc`.

## List of files

- **0-square_matrix_simple.py:**
  - a function that computes the square value of all integers of a matrix.
    - Prototype: `def square_matrix_simple(matrix=[]):`.
    - `matrix` is a 2 dimensional array.
    - Returns a new matrix:
      - Same size as `matrix`.
      - Each value should be the square of the value of the input.
    - Initial matrix should not be modified.

- **1-search_replace.py:**
  - a function that replaces all occurrences of an element by another in a new list.
    - Prototype: `def search_replace(my_list, search, replace):`.
    - `my_list` is the initial list.
    - `search` is the element to replace in the list.
    - `replace` is the new element.

- **2-uniq_add.py:**
  - a function that adds all unique integers in a list (only once for each integer).
    - Prototype: `def uniq_add(my_list=[]):`

- **3-common_elements.py:**
  - a function that returns a set of common elements in two sets.
    - Prototype: `def common_elements(set_1, set_2):`

- **4-only_diff_elements.py:**
  - a function that returns a set of all elements present in only one set.
    - Prototype: `def only_diff_elements(set_1, set_2):`

- **5-number_keys.py:**
  - a function that returns the number of keys in a dictionary.
    - Prototype: `def number_keys(a_dictionary):`

- **6-print_sorted_dictionary.py:**
  - a function that prints a dictionary by ordered keys.
    - Prototype: `def print_sorted_dictionary(a_dictionary):`.
    - Keys should be sorted by alphabetic order.
    - Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary).
    - Dictionary values can have any type.

- **7-update_dictionary.py:**
  - a function that replaces or adds key/value in a dictionary.
    - Prototype: `def update_dictionary(a_dictionary, key, value):`
    - `key` argument will be always a string.
    - `value` argument will be any type.
    - If a key exists in the dictionary, the value will be replaced.
    - If a key doesn’t exist in the dictionary, it will be created.

- **8-simple_delete.py:**
  - a function that deletes a key in a dictionary.
    - Prototype: `def simple_delete(a_dictionary, key=""):`
    - `key` argument will be always a string.
    - If a key doesn’t exist, the dictionary won’t change.

- **9-multiply_by_2.py:**
  - a function that returns a new dictionary with all values multiplied by 2
    - Prototype: `def multiply_by_2(a_dictionary):`
    - Returns a new dictionary.

- **10-best_score.py:**
  - a function that returns a key with the biggest integer value.
    - Prototype: `def best_score(a_dictionary):`
    - If no score found, return `None`.