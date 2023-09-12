#!/usr/bin/node
// A script that concats 2 files
// The first argument is the file path of the first source file
// The second argument is the file path of the second source file
// The third argument is the file path of the destination

// Import the fs module to work with files
const fs = require('fs');

// Get the file paths from the command line arguments
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

// Read the contents of fileA and fileB using the readFile() method of fs
fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) {
    // Handle any errors
    console.error(err);
    return;
  }
  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) {
      // Handle any errors
      console.error(err);
      return;
    }
    // Concatenate the contents of fileA and fileB using the + operator
    const dataC = dataA + dataB;
    // Write the concatenated data to fileC using the writeFile() method of fs
    fs.writeFile(fileC, dataC, 'utf8', (err) => {
      if (err) {
        // Handle any errors
        console.error(err);
      }
    });
  });
});
