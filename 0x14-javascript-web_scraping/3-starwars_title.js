#!/usr/bin/node

// Import the request module for making HTTP requests
const request = require('request');

// Construct the URL using the command line argument
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

// Send a request to the constructed URL
request(url, function (error, response, body) {
  // Log the error if it occurs, otherwise log the title of the film
  console.log(error || JSON.parse(body).title);
});
