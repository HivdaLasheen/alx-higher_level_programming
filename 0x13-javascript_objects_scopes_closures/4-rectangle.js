#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object if width or height are not valid
      this.width = undefined;
      this.height = undefined;
    }
  }

  print () {
    if (!this.width || !this.height) {
      return;
    }
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  double () {
    if (!this.width || !this.height) {
      return;
    }
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    if (!this.width || !this.height) {
      return;
    }
    [this.width, this.height] = [this.height, this.width];
  }
}

module.exports = Rectangle;
