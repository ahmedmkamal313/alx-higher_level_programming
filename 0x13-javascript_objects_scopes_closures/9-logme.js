#!/usr/bin/node
// Defines a function that prints the number of arguments already printed and the new argument value

// Export the function
exports.logMe = function (item) {
  // Initialize a variable to store the number of arguments already printed
  // Use a closure to keep the variable in scope
  let count = (function () {
    // Use a private variable to store the count
    let counter = 0;
    // Return a function that increments and returns the counter
    return function () {
      return counter++;
    };
  })();

  // Print the count and the item using a template literal
  console.log(`${count()}: ${item}`);
};
