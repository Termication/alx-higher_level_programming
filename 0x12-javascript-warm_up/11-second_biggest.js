#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const argumentCount = process.argv.length;
  const numbersArray = [];
  for (let i = 2; i < argumentCount; i++) {
    numbersArray[i - 2] = parseInt(process.argv[i]);
  }
  numbersArray.sort(function (a, b) { return b - a; });
  console.log(numbersArray[1]);
}
