#!/usr/bin/node

// Use process.argv to get the array of arguments passed to the script
const args = process.argv;
// Use args[2] to get the first argument, if it exists
const firstArg = args[2];
// Console
console.log(firstArg === undefined ? 'No argument' : firstArg);
