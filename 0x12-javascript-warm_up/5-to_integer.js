#!/usr/bin/node
// Use process.argv to get the array of arguments passed to the script
const args = process.argv;
// Use args[2] to get the first argument, if it exists
const arg = args[2];
// Use Number(arg) to convert the argument to a number, if possible
const num = Number(arg);
// Use Number.isInteger(num) to check if the number is an integer
const isInt = Number.isInteger(num);
// Console
console.log(isInt ? 'My number: ' + num : 'Not a number');
