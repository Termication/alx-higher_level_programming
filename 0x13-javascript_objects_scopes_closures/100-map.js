#!/usr/bin/node
const list = require('./100-data').list;

// Compute the new list using map
const newList = list.map((value, index) => value * index);

// Print the initial list
console.log(list);
console.log(newList);
