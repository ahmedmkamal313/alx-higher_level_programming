#!/usr/bin/node
//// Defines a class Rectangle with a constructor that takes 2 arguments w and h
// and checks if they are positive integers
class Rectangle {
  // Constructor that initializes the instance attributes width and height
  // or creates an empty object if w or h is 0 or not a positive integer
  constructor (w, h) {
    // Check if w and h are positive integers
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
    // Otherwise, create an empty object
    else { this.width = undefined;
    this.height = undefined;
    }
  }
}
// Export the class
module.exports = Rectangle;
