#!/usr/bin/node

// Import the request module for making HTTP requests
const request = require('request');

// Send a request to the URL provided as the first command line argument
request(process.argv[2], function (error, response, body) {
  // If no error occurs, proceed to parse and process the response body
  if (!error) {
    const todos = JSON.parse(body); // Parse the JSON response body
    const completed = {}; // Initialize an object to store the count of completed todos per user

    // Iterate over each todo item
    todos.forEach((todo) => {
      // If the todo is completed, update the count for the corresponding user
      if (todo.completed) {
        if (completed[todo.userId] === undefined) {
          completed[todo.userId] = 1; // Initialize count if not already present
        } else {
          completed[todo.userId] += 1; // Increment count
        }
      }
    });

    // Log the object containing counts of completed todos per user
    console.log(completed);
  }
});
