#!/usr/bin/node

const inputNumber = parseInt(process.argv[2]);
if (process.argv[2] === undefined || isNaN(inputNumber)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + inputNumber);
}
