#!/usr/bin/node

// Import the request module for making HTTP requests
const request = require('request');

// Send a GET request to the URL provided as the first command line argument
request.get(process.argv[2]).on('response', function (response) {
  // Log the status code of the response
  console.log(`code: ${response.statusCode}`);
});
