#!/usr/bin/node
const originalList = require('./100-data.js').list;
console.log(originalList);
const newList = originalList.map((item, index) => item * index);
console.log(newList);
