#!/bin/bash
# This script sends a PUT request to the specified URL to demonstrate HTTP protocol manipulation.
curl -s -L -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
