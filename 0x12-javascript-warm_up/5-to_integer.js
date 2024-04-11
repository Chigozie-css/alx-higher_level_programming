#!/usr/bin/node
// This script checks if the first command-line argument provided is a number and prints its parsed integer value.
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(process.argv[2]));
}
