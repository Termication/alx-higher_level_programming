#!/bin/bash

# This script sends a DELETE request to the URL passed as the first argument,
# and displays the body of the response.

# Send a DELETE request to the provided URL ($1)
# -s: Silent mode (suppress progress meter and error messages)
# -X DELETE: Specify the request method as DELETE
curl -sX DELETE "$1"
