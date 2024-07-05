#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the value of the 'X-Request-Id' variable found in the response headers.
"""

if __name__ == "__main__":
    import urllib.request as request
    from sys import argv

    # Ensure a URL is provided as an argument
    if len(argv) < 2:
        print("Usage: ./script.py <URL>")
        exit(1)

    url = argv[1]

    # Create a request object for the specified URL
    req = request.Request(url)

    # Send the request and get the response
    with request.urlopen(req) as response:
        # Print the value of the 'X-Request-Id' header
        print(response.headers.get('X-Request-Id'))
