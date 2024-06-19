#!/usr/bin/node
function findSecondBiggestInteger(args) {
  // Convert arguments to integers and filter out NaN
  const integers = args.map(arg => parseInt(arg)).filter(num => !isNaN(num));
  // Sort integers in descending order
  integers.sort((a, b) => b - a);
  // If there's no valid integer or only one integer, return 0
  if (integers.length <= 1) {
    return 0;
  }
  // Return the second element in the sorted array (second biggest integer)
  return integers[1];
}
const argumentsList = process.argv.slice(2); // Exclude first two arguments (node executable and script file)
console.log(findSecondBiggestInteger(argumentsList));
