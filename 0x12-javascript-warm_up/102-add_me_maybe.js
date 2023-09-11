#!/usr/bin/node
function addMeMaybe (number, theFunction) {
  // Use Number(number) to convert the argument to a number, if possible
  const num = Number(number);

  // Use num + 1 to increment the number by one
  const incremented = num + 1;

  // Use theFunction(incremented) to call the function with the incremented number as an argument
  theFunction(incremented);
}

// Use module.exports to export the function as an object property
module.exports = {
  addMeMaybe
};
