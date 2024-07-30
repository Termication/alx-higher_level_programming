#!/usr/bin/node

// Import the request module for making HTTP requests
const request = require('request');

// Construct the URL using the command line argument
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

// Send a request to the constructed URL to get film details
request(url, function (error, response, body) {
  if (!error) {
    // Parse the JSON response body to get the list of character URLs
    const characters = JSON.parse(body).characters;
    // Call the function to print character names, starting with the first character
    printCharacters(characters, 0);
  }
});

// Function to print character names recursively
function printCharacters(characters, index) {
  // Send a request to get details for the character at the current index
  request(characters[index], function (error, response, body) {
    if (!error) {
      // Parse the JSON response body to get character details and log the character name
      console.log(JSON.parse(body).name);
      // If there are more characters to process, call the function recursively for the next index
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
