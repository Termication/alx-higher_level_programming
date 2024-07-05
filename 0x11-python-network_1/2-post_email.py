#!/usr/bin/python3
"""
This script takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response.
"""

if __name__ == "__main__":
    import urllib.parse as parse
    import urllib.request as request
    from sys import argv

    # Ensure both URL and email are provided as arguments
    if len(argv) < 3:
        print("Usage: ./script.py <URL> <email>")
        exit(1)

    url = argv[1]
    email = argv[2]

    # Encode the email parameter
    values = {'email': email}
    data = parse.urlencode(values).encode('utf-8')

    # Create a POST request with the encoded data
    req = request.Request(url, data)

    # Send the request and get the response
    with request.urlopen(req) as response:
        # Print the body of the response, decoded as UTF-8
        print(response.read().decode('utf-8'))
