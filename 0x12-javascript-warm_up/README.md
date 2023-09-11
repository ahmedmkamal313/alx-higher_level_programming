# 0x12. JavaScript - Warm up
This project is an introduction to **JavaScript**, a high-level, interpreted scripting language that is widely used for web development. **JavaScript** can create dynamic and interactive web pages by manipulating the HTML and CSS elements. **JavaScript** can also be used for other purposes, such as server-side programming, game development, and graphic art.

In this project, we learned the basics of **JavaScript**, such as variables, data types, operators, control structures, functions, and modules. We also practiced writing scripts that can run on the **Node.js** platform, which allows us to execute **JavaScript** code outside of a web browser.

## Install Node 14
```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
### Install semi-standard
```
$ sudo npm install semistandard --global
```
## Files
The following files are scripts written in JavaScript. To run them, you need to have Node.js installed on your system. You can execute them with the command `node <file>`.

- [0-javascript_is_amazing.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x12-javascript-warm_up/0-javascript_is_amazing.js): This script prints “JavaScript is amazing” using a constant variable and the console.log function.
- [1-multi_languages.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x12-javascript-warm_up/1-multi_languages.js): This script prints 3 lines: “C is fun”, “Python is cool”, and “JavaScript is amazing” using 3 constant variables and the console.log function.
- [2-arguments.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x12-javascript-warm_up/2-arguments.js): This script prints a message depending on the number of arguments passed to it using the process.argv array and the console.log function.
- [3-value_argument.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x12-javascript-warm_up/3-value_argument.js): This script prints the first argument passed to it using the process.argv array and the console.log function. If no arguments are passed, it prints “No argument”.
- [4-concat.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x12-javascript-warm_up/4-concat.js): This script prints two arguments passed to it in the format “<arg1> is <arg2>” using the process.argv array and the console.log function.
- [5-to_integer.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x12-javascript-warm_up/5-to_integer.js): This script prints “My number: <first argument converted in integer>” if the first argument can be converted to an integer using the process.argv array, the Number function, and the console.log function. If the argument can’t be converted, it prints “Not a number”.
- [6-multi_languages_loop.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x12-javascript-warm_up/6-multi_languages_loop.js): This script prints 3 lines: “C is fun”, “Python is cool”, and “JavaScript is amazing” using an array of stri*ngs and a for loop.
- [7-multi_c.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x12-javascript-warm_up/7-multi_c.js): This script prints x times “C is fun” using the first argument of the script as x, the process.argv array, and a for loop. If x can’t be converted to an integer, it prints “Missing number of occurrences”.
- [8-square.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x12-javascript-warm_up/8-square.js): This script prints a square of size x using the first argument of the script as x, the process.argv array, and two nested for loops. If x can’t be converted to an integer, it prints “Missing size”.
- [9-add.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x12-javascript-warm_up/9-add.js): This script prints the addition of two integers using two arguments of the script as the integers, the process.argv array, a function named add, and the console.log function.
- [10-factorial.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x12-javascript-warm_up/10-factorial.js): This script computes and prints the factorial of a non-negative integer using the first argument of the script as the integer, the process.argv array, a recursive function named factorial, and the console.log function. If the argument can’t be converted to an integer or is negative, it returns NaN.
- [11-second_biggest.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x12-javascript-warm_up/11-second_biggest.js): This script searches and prints the second biggest integer in a list of arguments using the process.argv array, two variables named biggest and secondBiggest, a for loop, and the console.log function. If no arguments or only one argument are passed, it prints 0.
- [12-object.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x12-javascript-warm_up/12-object.js): This script updates an object by replacing its value property with 89 using dot notation.
- [13-add.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x12-javascript-warm_up/13-add.js): This file exports a function named add that returns the addition of two integers using module.exports. The function can be imported and used in another file with the require function.
- [100-let_me_const.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x12-javascript-warm_up/100-let_me_const.js): This file modifies the value of myVar to 333 using global object.
- [101-call_me_moby.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x12-javascript-warm_up/101-call_me_moby.js): This file exports a function named callMeMoby that executes x times a function using module.exports. The function can be imported and used in another file with the require function.
- [102-add_me_maybe.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x12-javascript-warm_up/102-add_me_maybe.js): This file exports a function named addMeMaybe that increments and calls a function using module.exports. The function can be imported and used in another file with the require function.
- [103-object_fct.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x12-javascript-warm_up/103-object_fct.js): This file adds a new function named incr to an object that increments its value property using dot notation.
