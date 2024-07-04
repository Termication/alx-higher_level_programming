#!/bin/bash

# This script takes a URL as an argument, sends a GET request to the URL,
# and displays the body of the response.

# Send a GET request to the provided URL ($1)
# -s: Silent mode (suppress progress meter and error messages)
# -L: Follow redirects if the requested URL has moved
curl -sL "$1"
