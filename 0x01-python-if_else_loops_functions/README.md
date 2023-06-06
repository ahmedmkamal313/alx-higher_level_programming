# **0x01. Python - if/else, loops, functions**

this project is a part of higher level programming from ALX SE.

**Requirements**
- Python Scripts
  - Allowed editors: vi, vim, emacs
  - All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
  - All files should end with a new line
  - The first line of all files should be exactly `#!/usr/bin/python3`
  - `README.md` file, at the root of the folder of the project, is mandatory
  - code should use the pycodestyle (version `2.8.*`)
  - All files must be executable
  - The length of files will be tested using `wc`
- C Scripts
  - Allowed editors: vi, vim, emacs
  - All files will be compiled on Ubuntu 20.04 LTS using gcc, using the options `-Wall -Werror -Wextra -pedantic -std=gnu89`
  - All files should end with a new line
  - code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
  - not allowed to use global variables
  - No more than 5 functions per file

**list of files**
**0-positive_or_negative.py:**
This program will assign a random signed `number` to the variable `number` each time it is executed.
```
#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
```
- The output of the program should be:
  - The number, followed by
    - if the number is greater than 0: `is positive`
    - if the number is 0: is `zero`
    - if the number is less than 0: `is negative`
  - followed by a new line.

**1-last_digit.py:**
This program will assign a random signed number to the variable number each time it is executed.
```
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
```
- The output of the program should be:
  - The string Last digit of, followed by
  - the number, followed by
  - the string is, followed by the last digit of number, followed by
    - if the last digit is greater than 5: the string `and is greater than 5`
    - if the last digit is 0: the string `and is 0`
    - if the last digit is less than 6 and not 0: the string `and is less than 6 and not 0`
  - followed by a new line

