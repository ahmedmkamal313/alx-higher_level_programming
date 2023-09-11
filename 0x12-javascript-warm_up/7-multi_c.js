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
  // The argument is a positive integer, print "C is fun" x times
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  // The argument is not a positive integer, print "Missing number of occurrences"
  console.log('Missing number of occurrences');
}
