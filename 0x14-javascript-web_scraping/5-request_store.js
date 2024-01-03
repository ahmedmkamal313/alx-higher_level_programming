#!/usr/bin/node
// A script that gets the contents of a webpage and stores it in a file.

// Import the request and fs modules
const request = require('request');
const fs = require('fs');

// Get the URL to request from the first argument
const url = process.argv[2];

// Get the file path to store the body response from the second argument
const filePath = process.argv[3];

// Make a GET request to the URL
request.get(url, (err, response, body) => {
  // If an error occurred, print the error object
  if (err) {
    console.error(err);
  } else {
    // Otherwise, write the body response to the file in UTF-8 encoding
    fs.writeFile(filePath, body, 'utf8', (err) => {
      // If an error occurred, print the error object
      if (err) {
        console.error(err);
      } else {
        // Otherwise, print a success message
        console.log('The file was saved!');
      }
    });
  }
});
