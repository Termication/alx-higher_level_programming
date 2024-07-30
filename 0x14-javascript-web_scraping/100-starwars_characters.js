#!/usr/bin/node

// Import the request module for making HTTP requests
const request = require('request');

// Construct the URL using the command line argument
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

// Initialize an object to store character details
let def = {};

// Send a request to the constructed URL to get film details
request(url, function (error, response, body) {
  if (error) {
    // Log any error that occurs during the request
    console.log(error);
  } else {
    // Parse the JSON response body to get film details
    const abc = JSON.parse(body);
    
    // Iterate over each character URL in the film details
    abc.characters.forEach(function (item) {
      // Send a request to get details for each character
      request(item, function (error, response, content) {
        if (error) {
          // Log any error that occurs during the character request
          console.log(error);
        } else {
          // Parse the JSON response body to get character details
          def = JSON.parse(content);
          // Log the character name
          console.log(def.name);
        }
      });
    });
  }
});
