#!/usr/bin/node
const Square = require('./5-square');

class Square1 extends Square {
  charPrint (char) {
    if (char === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(char.repeat(this.width));
      }
    }
  }
}

module.exports = Square1;
