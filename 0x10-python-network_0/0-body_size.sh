#!/bin/bash

# Get the URL from the command-line argument
URL=$1

# Send a request to the URL, retrieve the response, and extract the size of the body in bytes
curl -s -o /dev/null -w "%{size_download}\n" "$URL"
