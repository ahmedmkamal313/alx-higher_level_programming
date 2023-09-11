#!/usr/bin/node
// Use process.argv to get the array of arguments passed to the script
const args = process.argv;

// Use args[2] to get the first argument, if it exists
const arg = args[2];

// Use Number(arg) to convert the argument to a number, if possible
const num = Number(arg);

// Use Number.isInteger(num) and num > 0 to check if the number is a positive integer
const isPosInt = Number.isInteger(num) && num > 0;

// Use if-else statements to print different messages based on isPosInt
if (isPosInt) {
  // The argument is a positive integer, print a square of size num
  // Declare a constant string with the character X
  const char = 'X';

  // Use a for loop to iterate num times
  for (let i = 0; i < num; i++) {
    // Declare an empty string to store the row of the square
    let row = '';

    // Use another for loop to iterate num times
    for (let j = 0; j < num; j++) {
      // Append the char to the row
      row += char;
    }

    // Use console.log(...) to print the row
    console.log(row);
  }
} else {
  // The argument is not a positive integer, print "Missing size"
  console.log('Missing size');
}
