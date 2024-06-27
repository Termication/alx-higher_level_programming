#!/usr/bin/node

let numberOfOccurrences = parseInt(process.argv[2]);
if (isNaN(numberOfOccurrences) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  while (numberOfOccurrences > 0) {
    console.log('C is fun');
    numberOfOccurrences--;
  }
}
