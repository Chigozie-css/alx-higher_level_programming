#!/usr/bin/node
// This script prints 'C is fun' a specified number of times.
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
	console.log('Missing number of occurrences');
} else {
	const x = Number(process.argv[2]);
	// Convert the command-line argument to a number
	let i = 0;
	while (i < x)
	{
		console.log('C is fun');
		i++;
	}
}
