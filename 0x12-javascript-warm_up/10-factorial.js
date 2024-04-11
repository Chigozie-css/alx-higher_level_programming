#!/usr/bin/node
// This function calculates the factorial of a given number.
function factorial(n) {
  if (n < 0) {
    return -1; // Return -1 if n is negative
  }
  if (n === 0 || isNaN(n)) {
    return 1; // Return 1 if n is 0 or not a number
  }
  return n * factorial(n - 1);
}
console.log(factorial(Number(process.argv[2])));
