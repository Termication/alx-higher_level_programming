#!/usr/bin/python3
"""Script that sends a POST request to a specified
URL and processes the response."""

import requests  # Import the requests library to handle HTTP requests
from sys import argv  # Import argv from sys to access command-line arguments

if __name__ == '__main__':
    # Define the URL to send the POST request to
    url = "http://0.0.0.0:5000/search_user"

    # Otherwise, use an empty string as the value
    data = {"q": argv[1][0] if len(argv) > 1 else ""}

    # Send a POST request to the specified URL with the data
    response = requests.post(url, data=data)

    try:
        # Try to parse the response as JSON
        d = response.json()

        # Check if the JSON response is empty
        if not d:
            print("No result")
        else:
            # If the JSON response is not empty, print the id and name from the
            # response
            print("[{}] {}".format(d.get("id"), d.get("name")))
    except ValueError:
        # If the response is not a valid JSON, print an error message
        print("Not a valid JSON")
