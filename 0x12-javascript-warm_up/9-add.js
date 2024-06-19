#!/usr/bin/node

function add(a, b) {
  if (!isNaN(a) && !isNaN(b)) {
    console.log(a + b);
  } else {
    console.log('Invalid input. Please provide two integers.');
  }
}

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

add(arg1, arg2);
