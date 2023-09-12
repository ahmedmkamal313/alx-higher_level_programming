#!/usr/bin/node
// Defines a function that prints the number of arguments already printed and the new argument value

// The number is incremented by one each time the function is called
// Declare and initialize a count variable to keep track of the number of calls
let count = 0;
exports.logMe = function (item) {
  // Define and export the logMe function
  console.log(`${count++}: ${item}`);
  // Use template literals to log the count and the item, and increment the count by one
};
