#!/usr/bin/node
function add(a, b) {
  // Use Number(a) and Number(b) to convert the arguments to numbers, if possible
  const num1 = Number(a);
  const num2 = Number(b);

  // calculate the sum of the numbers
  const sum = num1 + num2;

  // Return the sum
  return sum;
}
// Use module.exports to export the function as an object property
module.exports = {
  add: add
};
