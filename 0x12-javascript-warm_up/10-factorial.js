#!/usr/bin/node
function computeFactorial(num) {
  // Base case: factorial of 0 or NaN is 1
  return num === 0 || isNaN(num) ? 1 : num * computeFactorial(num - 1);
}
const inputNumber = Number(process.argv[2]);
console.log(computeFactorial(inputNumber));
