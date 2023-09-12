#!/usr/bin/node
// Defines a class Square that defines a square and inherits from Rectangle of 4-rectangle.js
// Import the class Rectangle from 4-rectangle.js
const Rectangle = require('./4-rectangle');
// Define a class Square that extends Rectangle
class Square extends Rectangle {
  // Constructor that takes 1 argument: size
  constructor (size) {
    // Call the constructor of Rectangle with size as both width and height
    super(size, size);
  }
}

// Export the class
module.exports = Square;
