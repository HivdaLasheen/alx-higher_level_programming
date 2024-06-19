#!/usr/bin/node

function addIntegers(num1, num2) {
  return num1 + num2;
}

const firstInt = parseInt(process.argv[2]);
const secondInt = parseInt(process.argv[3]);

if (!isNaN(firstInt) && !isNaN(secondInt)) {
  console.log(addIntegers(firstInt, secondInt));
} else {
  console.log('Please provide two valid integers.');
}
