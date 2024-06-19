#!/usr/bin/node
module.exports = class Square extends require('./4-rectangle.js') {
  constructor(size) {
    super(size, size); // Call the constructor of Rectangle with size for both width and height
  }
};
