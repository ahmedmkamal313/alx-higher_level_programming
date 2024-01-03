#!/usr/bin/node
// Import the fs module
var fs = require('fs');

// Get the file path from the first argument
var filePath = process.argv[2];

// Read the file asynchronously
fs.readFile(filePath, 'utf-8', function (err, data) {
  // If an error occurred, print the error object
  if (err) {
    console.log(err);
  }
  // Otherwise, print the content of the file
  else {
    console.log(data);
  }
});
