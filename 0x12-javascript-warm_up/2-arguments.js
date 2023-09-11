#!/usr/bin/node

// Use process.argv to get the array of arguments passed to the script
const args = process.argv;
// Use args.length to get the number of arguments
const numArgs = args.length;
// console log
console.log(numArgs === 2 ? 'No argument' : numArgs === 3 ? 'Argument found' : 'Arguments found');
