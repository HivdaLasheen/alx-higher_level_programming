#!/usr/bin/node
function addIntegers(num1, num2) {
  return num1 + num2;
}
console.log(addIntegers(Number(process.argv[2]), Number(process.argv[3])));
