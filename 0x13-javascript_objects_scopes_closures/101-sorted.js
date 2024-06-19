#!/usr/bin/node

// Import the dictionary from 101-data.js
const { dict } = require('./101-data.js');

// Initialize an empty object to store the new dictionary
const newDict = {};

// Iterate over each key-value pair in the original dictionary
for (const [userId, occurrences] of Object.entries(dict)) {
  // If the number of occurrences is not yet a key in newDict, create it and set its value to an empty array
  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }
  // Push the userId to the array corresponding to the number of occurrences
  newDict[occurrences].push(userId);
}

// Print the new dictionary
console.log(newDict);
