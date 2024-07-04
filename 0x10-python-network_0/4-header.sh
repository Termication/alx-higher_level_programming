#!/bin/bash

# This script takes a URL as an argument, sends a GET request to the URL,
# and displays the body of the response.
# A header variable X-School-User-Id must be sent with the value 98.

# Send a GET request to the provided URL ($1)
# -s: Silent mode (suppress progress meter and error messages)
# -X GET: Specify the request method as GET
# -H "X-School-User-Id: 98": Add a custom header with the name 'X-School-User-Id' and the value '98'
curl -sX GET -H "X-School-User-Id: 98" "$1"
