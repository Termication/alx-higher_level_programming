#!/bin/bash
# Get the URL from the command-line argument
# Send a request to the URL, retrieve the response, and extract the size of the body in bytes
curl -s "$1" | wc -c
