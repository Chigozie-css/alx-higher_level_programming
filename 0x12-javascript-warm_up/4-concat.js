#!/usr/bin/node
// This script concatenates the third and fourth command-line arguments provided when executing the script.
if (process.argv.length >= 4) {
	console.log(process.argv[2] + ' is ' + process.argv[3]);
} else {
	console.log('Please provide both arguments.');
}
