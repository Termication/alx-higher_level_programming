#!/usr/bin/node

// Import the file system module
const fs = require('fs');

// Write the content (process.argv[3]) to the specified file (process.argv[2])
fs.writeFile(process.argv[2], process.argv[3], error => {
  // Log any errors that occur during the write process
  if (error) console.log(error);
});
