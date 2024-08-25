#!/bin/bash
# This script takes a URL as an argument, sends a GET request to the URL,
# and displays the body of the response.
# A header variable X-School-User-Id must be sent with the value
curl -sX GET -H "X-School-User-Id: 98" "$1"
