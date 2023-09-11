#!/usr/bin/node
// Define a function that return the addition of 2 integers
function add (a, b) {
  // Use Number() to convert the arguments to numbers, if possible
  const num1 = Number(a);
  const num2 = Number(b);
  // declare variable and assign the result of addition
  const sum = num1 + num2;
  // Return the result of addition
  return sum;
}
// Use process.argv to get the array of arguments passed to the script
const args = process.argv;
// Use args[2] and args[3] to get the first and second arguments, if they exist
const arg1 = args[2];
const arg2 = args[3];
const result = add(arg1, arg2);
// print the result
console.log(result);
