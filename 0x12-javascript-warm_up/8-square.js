#!/usr/bin/node

let rectangleSize = parseInt(process.argv[2]);
if (isNaN(rectangleSize) || process.argv[2] === undefined) {
  console.log('Missing size');
}
let patternString = 'X';
for (let i = 0; i < rectangleSize - 1; i++) {
  patternString += 'X';
}
while (rectangleSize > 0) {
  console.log(patternString);
  rectangleSize--;
}
