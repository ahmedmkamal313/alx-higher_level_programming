#!/usr/bin/node
// The module.exports statement exports the Square class as a module
module.exports = class Square extends require('./5-square.js') {
  // The charPrint method takes a character c as an argument and prints the square using that character
  // If c is undefined, it calls the print method from the parent class
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      // Use a for loop to print c repeated width times for each row of the square
      for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
    }
  }
};
