#!/usr/bin/node

// Import the request module for making HTTP requests
const request = require('request');

// Send a request to the URL provided as the first command line argument
request(process.argv[2], function (error, response, body) {
  // If no error occurs, proceed to parse and process the response body
  if (!error) {
    const results = JSON.parse(body).results;
    // Count the number of movies where a character URL ends with '/18/'
    const count = results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0);
    // Log the count
    console.log(count);
  }
});
