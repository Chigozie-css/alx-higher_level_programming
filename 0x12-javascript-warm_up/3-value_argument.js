#!/usr/bin/node
// This script checks if an argument is provided and prints it. If no argument is provided, it prints 'No argument'.
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
