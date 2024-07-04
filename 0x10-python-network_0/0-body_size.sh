#!/bin/bash

# This script takes a URL as an argument, sends a request to that URL,
# and displays the size of the body of the response.

# Send a request to the provided URL ($1) and get only the response headers (-I)
# Use grep to find the line containing 'Content-Length:'
# Use cut to extract the size value (second field)
curl -sI "$1" | grep 'Content-Length:' | cut -d' ' -f2
