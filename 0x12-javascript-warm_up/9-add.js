#!/usr/bin/node
// This function adds two numbers and prints the result.
function add(a, b) {
  const c = a + b;
  console.log(c);
}

add(Number(process.argv[2]), Number(process.argv[3]));
