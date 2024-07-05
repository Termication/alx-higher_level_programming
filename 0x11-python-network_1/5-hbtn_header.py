#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the value of the 'X-Request-Id' variable found in the response header.
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    # Ensure a URL is provided as an argument
    if len(argv) < 2:
        print("Usage: ./script.py <URL>")
        exit(1)

    url = argv[1]

    # Send a GET request to the specified URL
    response = requests.get(url)

    # Print the value of the 'X-Request-Id' header
    print(response.headers.get('X-Request-Id'))
