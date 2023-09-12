#!/usr/bin/node
// Defines a class Rectangle with a constructor that takes 2 arguments w and h
// and checks if they are positive integers
// and an instance method print() that prints the rectangle using the character X
class Rectangle {
  // Constructor that initializes the instance attributes width and height
  // or creates an empty object if w or h is 0 or not a positive integer
  constructor (w, h) {
    // Check if w and h are positive integers
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Instance method print() that prints the rectangle using the character X
  print () {
    // Loop through the height of the rectangle
    for (let i = 0; i < this.height; i++) {
      // Initialize an empty string to store the row of X's
      let row = '';
      // Loop through the width of the rectangle
      for (let j = 0; j < this.width; j++) {
        // Append an X to the row string
        row += 'X';
      }
      // Print the row string
      console.log(row);
    }
  }
}
// Export the class
module.exports = Rectangle;
