#!/usr/bin/node

// Import the fs module for file system operations
const fs = require('fs');

// Import the request module for making HTTP requests
const request = require('request');

// Send a request to the URL provided as the first command line argument
// Pipe the response to a file specified by the second command line argument
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
