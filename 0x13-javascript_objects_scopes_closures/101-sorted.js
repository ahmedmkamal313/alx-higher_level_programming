#!/usr/bin/node
// A script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence

// Import the dict from the file 101-data.js
const dict = require('./101-data').dict;

// Initialize an empty object to store the new dictionary
const newDict = {};

// Loop through the keys and values of the dict
for (const [key, value] of Object.entries(dict)) {
  // Check if the value is already a key in the new dictionary
  if (newDict[value]) {
    // If yes, push the key to the corresponding array
    newDict[value].push(key);
  } else {
    // If not, create a new array with the key as the first element
    newDict[value] = [key];
  }
}

// Print the new dictionary at the end
console.log(newDict);
