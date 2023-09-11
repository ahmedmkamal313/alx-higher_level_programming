#!/usr/bin/node
// Use process.argv to get the array of arguments passed to the script
const args = process.argv;
// Use args[2] and args[3] to get the first and second arguments, if they exist
const arg1 = args[2];
const arg2 = args[3];
// Console
console.log(arg1 + ' is ' + arg2);
