#!/usr/bin/node

function findSecondBiggest (args) {
  if (args.length <= 1) {
    return 0;
  }

  const numbers = args.map(Number).sort((a, b) => b - a);
  return numbers[1];
}

const args = process.argv.slice(2);

console.log(findSecondBiggest(args));
