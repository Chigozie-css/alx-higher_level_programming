#!/usr/bin/node
// This script prints a square of 'X' characters with the side length specified by the command-line argument.
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const x = Number(process.argv[2]); // Convert the command-line argument to a number
  let i = 0;
  while (i < x) {
    console.log('X'.repeat(x)); // Print a line of 'X' characters repeated 'x' times
    i++;
  }
}
