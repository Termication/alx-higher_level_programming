#!/bin/bash

# This script sends a PUT request to the specified URL to demonstrate HTTP protocol manipulation.
# It sends specific data and headers to a local server to trigger a specific response.

# Send a PUT request to the URL 0.0.0.0:5000/catch_me
# -s: Silent mode (suppress progress meter and error messages)
# -L: Follow redirects if the requested URL has moved
# -X PUT: Specify the request method as PUT
# -d "user_id=98": Send the data "user_id=98" in the request body
# -H "Origin: HolbertonSchool": Set the Origin header to "HolbertonSchool"
curl -s -L -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
