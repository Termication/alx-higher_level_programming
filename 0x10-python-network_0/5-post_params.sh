#!/bin/bash

# This script takes a URL as an argument, sends a POST request to the URL,
# and displays the body of the response.
# Two variables must be sent in the request body:
# - email with the value 'test@gmail.com'
# - subject with the value 'I will always be here for PLD'

# Send a POST request to the provided URL ($1)
# -s: Silent mode (suppress progress meter and error messages)
# -X POST: Specify the request method as POST
# -d "email=test@gmail.com&subject=I will always be here for PLD": Send the specified data in the request body
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
