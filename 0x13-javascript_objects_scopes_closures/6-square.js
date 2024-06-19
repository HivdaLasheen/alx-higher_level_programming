#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint(c) {
    if (c === undefined) {
      c = 'X'; // Default character is 'X' if c is undefined
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width)); // Print the square using the specified character
    }
  }
};
