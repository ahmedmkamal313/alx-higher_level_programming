#!/usr/bin/node
// Use process.argv to get the array of arguments passed to the script
const args = process.argv.slice(2); // Use slice(2) to remove the first two elements (node command and file name)
// Use args.length to get the number of arguments
const numArgs = args.length;

// Use if-else statements to handle different cases based on numArgs
if (numArgs <= 1) {
  // No argument or only one argument passed, print 0
  console.log(0);
} else {
  // More than one argument passed, search for the second biggest integer
  // Use Math.max(...args) to get the maximum value in the array of arguments
  const max = Math.max(...args);
  // Use args.filter(num => num < max) to get a new array with only the elements that are less than the maximum value
  const filtered = args.filter(num => num < max);
  // Use Math.max(...filtered) to get the maximum value in the filtered array, which is the second biggest integer in the original array
  const secondMax = Math.max(...filtered);
  // Use console.log(...) to print the second biggest integer
  console.log(secondMax);
}
