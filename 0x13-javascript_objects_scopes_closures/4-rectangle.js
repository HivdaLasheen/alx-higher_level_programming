#!/usr/bin/node
module.exports = class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object if w or h is not a positive integer or equal to 0
      this.width = undefined;
      this.height = undefined;
    }
  }

  print() {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  rotate() {
    if (this.width && this.height) {
      [this.width, this.height] = [this.height, this.width];
    }
  }

  double() {
    if (this.width && this.height) {
      [this.width, this.height] = [this.width * 2, this.height * 2];
    }
  }
};
