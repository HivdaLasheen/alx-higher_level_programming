#!/usr/bin/node
const numberOfOccurrences = Math.floor(Number(process.argv[2]));
if (isNaN(numberOfOccurrences)) {
  console.log('Missing number of occurrences');
} else {
  for (let count = 0; count < numberOfOccurrences; count++) {
    console.log('C is fun');
  }
}
