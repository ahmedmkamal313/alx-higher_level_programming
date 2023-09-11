#!/usr/bin/node

function factorial (n) {
  // Use Number(n) to convert the argument to a number, if possible
  const num = Number(n);
  // Use Number.isInteger(num) and num >= 0 to check if the number is a non-negative integer
  const isNonNegInt = Number.isInteger(num) && num >= 0;

  // Use if-else statements to handle different cases based on isNonNegInt
  if (isNonNegInt) {
    // The argument is a non-negative integer, compute the factorial recursively
    if (num === 0 || num === 1) {
      // Base case: the factorial of 0 or 1 is 1
      return 1;
    } else {
      // Recursive case: the factorial of n is n times the factorial of n - 1
      return num * factorial(num - 1);
    }
  } else {
    // The argument is not a non-negative integer, check if it is NaN
    if (Number.isNaN(num)) {
      // The argument is NaN, return 1
      return 1;
    } else {
      // The argument is neither a non-negative integer nor NaN, return NaN
      return NaN;
    }
  }
}

// Use process.argv to get the array of arguments passed to the script
const args = process.argv;
// Use args[2] to get the first argument, if it exists
const arg = args[2];
// Use factorial(arg) to call the function with the argument
const result = factorial(arg);
// Use console.log(...) to print the result
console.log(result);
