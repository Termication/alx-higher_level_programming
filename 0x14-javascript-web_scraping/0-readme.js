#!/usr/bin/node

// Import the fs module for file system operations
const fs = require('fs');

// Read the file specified by the first command line argument
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  // Output the error if it occurs, otherwise output the file content
  console.log(error || content);
});
