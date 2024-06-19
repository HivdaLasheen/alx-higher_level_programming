#!/usr/bin/node

function add(a, b) {
  return a + b;
}

const firstInteger = Number(process.argv[2]);
const secondInteger = Number(process.argv[3]);

if (isNaN(firstInteger) || isNaN(secondInteger)) {
  console.log('Arguments are not valid integers');
} else {
  console.log(`The addition of ${firstInteger} and ${secondInteger} is: ${add(firstInteger, secondInteger)}`);
}
