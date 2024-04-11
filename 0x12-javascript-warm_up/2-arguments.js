#!/usr/bin/node
// This script checks the number of arguments passed to it and prints a corresponding message.
if (process.argv.length === 2) {
	console.log('No argument');
} else if (process.argv.length === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
