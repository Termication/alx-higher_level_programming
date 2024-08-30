#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument,
# and displays the body of the response.
# The JSON data to be sent is read from a file specified as the second argument.
curl -s -H "Content-Type: application/json" -d @"$(cat $2)" "$1"
