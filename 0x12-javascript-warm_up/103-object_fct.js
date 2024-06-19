#!/usr/bin/node
const newObj = {
  type: 'object',
  value: 12
};
console.log(newObj);
newObj.incr = function () {
  this.value++;
};
newObj.incr();
console.log(newObj);
newObj.incr();
console.log(newObj);
newObj.incr();
console.log(newObj);
