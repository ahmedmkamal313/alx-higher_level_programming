#!/usr/bin/node

function callMeMoby (x, theFunction) {
  // Use Number(x) to convert the argument to a number, if possible
  const num = Number(x);

  // Use Number.isInteger(num) and num > 0 to check if the number is a positive integer
  const isPosInt = Number.isInteger(num) && num > 0;

  // Use if-else statements to handle different cases based on isPosInt
  if (isPosInt) {
    // The argument is a positive integer, execute the function x times
    // Use a for loop to iterate x times
    for (let i = 0; i < x; i++) {
      // Use theFunction() to call the function
      theFunction();
    }
  }
}

// Use module.exports to export the function as an object property
module.exports = {
  callMeMoby
};
