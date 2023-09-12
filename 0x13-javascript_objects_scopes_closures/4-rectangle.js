#!/usr/bin/node
// Defines a class Rectangle with a constructor that takes 2 arguments w and h
// and checks if they are positive integers
// and instance methods print(), rotate(), and double() that perform different operations on the rectangle
class Rectangle {
  // Constructor that initializes the instance attributes width and height
  // or creates an empty object if w or h is 0 or not a positive integer
  constructor (w, h) {
  // Checks if w & h are positive integers
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
      // loop throught the width of the rectangle
      for (let j = 0; j < this.width; j++) {
        // Append an X to the row string
        row += 'X';
      }
      // Print the row string
      console.log(row);
    }
  }

  // Instance method rotate() that exchanges the width and the height of the rectangle
  rotate () {
    // Swap the values of width and height using a temporary variable
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // Instance method double() that multiples the width and the height of the rectangle by 2
  double () {
    // Multiply the width and height by 2 using the assignment operator *=
    this.width *= 2;
    this.height *= 2;
  }
}

// Export the class
module.exports = Rectangle;
