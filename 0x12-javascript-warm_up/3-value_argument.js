#!/usr/bin/node

const originalProcess = process;

const myProcess = originalProcess;

if (myProcess.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(myProcess.argv[2]);
}
