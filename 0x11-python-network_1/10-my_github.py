#!/usr/bin/python3
"""A script that retrieves the user ID from
the GitHub API using basic authentication."""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # Create an authentication object using command-line arguments
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    # Send a GET request to the GitHub API with authentication
    r = requests.get("https://api.github.com/user", auth=auth)

    # Print the user ID from the JSON response
    print(r.json().get("id"))
