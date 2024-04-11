#!/usr/bin/node
// This function adds two numbers and prints the result.
function add(a, b) {
  const c = a + b; // Calculate the sum of the two numbers
  console.log(c); // Print the result to the console
}

// Call the add function with the first and second command-line arguments as numbers
add(Number(process.argv[2]), Number(process.argv[3]));
