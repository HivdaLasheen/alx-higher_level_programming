#!/usr/bin/node
const occurrences = require('./101-data.js').dict;
const userIdsByOccurrences = {};
for (const userId in occurrences) {
  const occurrence = occurrences[userId];
  if (userIdsByOccurrences[occurrence] === undefined) {
    userIdsByOccurrences[occurrence] = [userId];
  } else {
    userIdsByOccurrences[occurrence].push(userId);
  }
}
console.log(userIdsByOccurrences);
