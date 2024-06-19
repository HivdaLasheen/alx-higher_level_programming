#!/usr/bin/node
const sizeOfSquare = Math.floor(Number(process.argv[2]));
if (isNaN(sizeOfSquare)) {
  console.log('Missing size');
} else {
  for (let row = 0; row < sizeOfSquare; row++) {
    let line = '';
    for (let col = 0; col < sizeOfSquare; col++) {
      line += 'X';
    }
    console.log(line);
  }
}
