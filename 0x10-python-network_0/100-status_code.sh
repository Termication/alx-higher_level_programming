#!/bin/bash

# This script sends a request to a URL passed as an argument,
# and displays only the status code of the response.

# Send a request to the provided URL ($1)
# -s: Silent mode (suppress progress meter and error messages)
# -o /dev/null: Redirect the response body to /dev/null (ignore it)
# --write-out "%{http_code}": Output the HTTP status code of the response
curl -so /dev/null --write-out "%{http_code}" "$1"
