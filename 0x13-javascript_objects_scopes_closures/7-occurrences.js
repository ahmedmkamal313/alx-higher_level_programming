#!/usr/bin/node
// Defines a function that returns the number of occurrences in a list

// Export the function
exports.nbOccurences = function (list, searchElement) {
  // Initialize a variable to store the count of occurrences
  let count = 0;
  // Loop through the list
  for (let i = 0; i < list.length; i++) {
    // Check if the current element is equal to the search element
    if (list[i] === searchElement) {
      // Increment the count by 1
      count++;
    }
  }
  // Return the count
  return count;
};
