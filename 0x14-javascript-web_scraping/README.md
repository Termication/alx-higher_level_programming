# JSON Data Manipulation and API Requests

## Description

This project demonstrates how to manipulate JSON data, use the `request` and `fetch` APIs to make HTTP requests, and read and write files using the `fs` module in Node.js. The project is designed to help beginners understand these fundamental concepts in JavaScript and Node.js.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Usage](#usage)
   - [Manipulating JSON Data](#manipulating-json-data)
   - [Using Request and Fetch API](#using-request-and-fetch-api)
   - [Reading and Writing Files with FS Module](#reading-and-writing-files-with-fs-module)
4. [Contributing](#contributing)
5. [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Node.js and npm (Node Package Manager).
- You have a basic understanding of JavaScript.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/json-api-fs-tutorial.git
    ```
2. Navigate to the project directory:
    ```bash
    cd json-api-fs-tutorial
    ```
3. Install the required dependencies:
    ```bash
    npm install
    ```

## Usage

### Manipulating JSON Data

To manipulate JSON data, you can use JavaScript's built-in `JSON` object, which provides methods for parsing and stringifying JSON.

Example code:
```javascript
const jsonData = '{"name": "John", "age": 30, "city": "New York"}';

// Parse JSON string into an object
const obj = JSON.parse(jsonData);
console.log(obj.name); // Output: John

// Modify the object
obj.age = 31;

// Convert the object back to a JSON string
const newJsonData = JSON.stringify(obj);
console.log(newJsonData); // Output: {"name":"John","age":31,"city":"New York"}

Using Request and Fetch API
Request

You can use the request module to make HTTP requests in Node.js.

Example code:

javascript

const request = require('request');

request('https://api.example.com/data', { json: true }, (err, res, body) => {
    if (err) { return console.log(err); }
    console.log(body);
});

Fetch

You can use the fetch API in the browser or with the node-fetch module in Node.js.

Example code:

javascript

const fetch = require('node-fetch');

fetch('https://api.example.com/data')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));

Reading and Writing Files with FS Module

The fs module in Node.js allows you to interact with the file system.
Reading a File

Example code:

javascript

const fs = require('fs');

fs.readFile('example.json', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});

Writing to a File

Example code:

javascript

const fs = require('fs');

const data = JSON.stringify({ name: "Jane", age: 25 });

fs.writeFile('example.json', data, (err) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log('File has been written');
});

Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
License

This project is licensed under the MIT License - see the LICENSE file for details.

bash


### 2. `package.json`

```json
{
  "name": "json-api-fs-tutorial",
  "version": "1.0.0",
  "description": "A project to demonstrate JSON manipulation, API requests, and file operations using fs module.",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "node-fetch": "^2.6.7",
    "request": "^2.88.2"
  },
  "author": "Your Name",
  "license": "MIT"
}

3. index.js

javascript

const fs = require('fs');
const request = require('request');
const fetch = require('node-fetch');

// JSON Manipulation
const jsonData = '{"name": "John", "age": 30, "city": "New York"}';
const obj = JSON.parse(jsonData);
console.log('Original Object:', obj);

obj.age = 31;
const newJsonData = JSON.stringify(obj);
console.log('Updated JSON Data:', newJsonData);

// Writing JSON to a file
fs.writeFile('example.json', newJsonData, (err) => {
    if (err) {
        console.error('Error writing file:', err);
        return;
    }
    console.log('File has been written');

    // Reading JSON from a file
    fs.readFile('example.json', 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading file:', err);
            return;
        }
        console.log('Read from file:', data);
    });
});

// Using Request module to make an HTTP request
request('https://api.example.com/data', { json: true }, (err, res, body) => {
    if (err) {
        console.error('Error making request:', err);
        return;
    }
    console.log('Response from request:', body);
});

// Using Fetch API to make an HTTP request
fetch('https://api.example.com/data')
    .then(response => response.json())
    .then(data => console.log('Response from fetch:', data))
    .catch(error => console.error('Error:', error));

4. example.json

Create an empty example.json file for demonstration purposes. This file will be used to read and write JSON data.

json

{}

Instructions to Upload to GitHub

    Initialize Git and Commit Files

    bash

cd json-api-fs-tutorial
git init
git add .
git commit -m "Initial commit"

Create a New Repository on GitHub

Go to GitHub and create a new repository named json-api-fs-tutorial.

Add Remote and Push to GitHub

bash

git remote add origin https://github.com/your-username/json-api-fs-tutorial.git
git branch -M main
git push -u origin main
