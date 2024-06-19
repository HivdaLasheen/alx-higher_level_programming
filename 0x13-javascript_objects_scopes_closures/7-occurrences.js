#!/usr/bin/node

exports.nbOccurences = function (array, elementToFind) {
  let occurrenceCount = 0;
  array.forEach((currentElement) => {
    if (currentElement === elementToFind) {
      occurrenceCount++;
    }
  });
  return occurrenceCount;
};
