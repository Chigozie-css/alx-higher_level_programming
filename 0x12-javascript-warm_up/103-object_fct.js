#!/usr/bin/node
/*
  This script demonstrates object manipulation with a custom method.
*/

const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

myObject.incr = function () {
  this.value++;
};

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
