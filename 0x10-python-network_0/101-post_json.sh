#!/bin/bash

# This script sends a JSON POST request to a URL passed as the first argument,
# and displays the body of the response.
# The JSON data to be sent is read from a file specified as the second argument.

# Send a POST request to the provided URL ($1)
# -s: Silent mode (suppress progress meter and error messages)
# -X POST: Specify the request method as POST
# -H "Content-Type: application/json": Set the content type to application/json
# -d @"$2": Send the JSON data read from the file specified as the second argument ($2)
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
