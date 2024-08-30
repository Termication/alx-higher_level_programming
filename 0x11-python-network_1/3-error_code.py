#!/usr/bin/python3
"""
This script takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response.
"""

if __name__ == "__main__":
    import urllib.error as error  # To handle HTTP errors
    import urllib.request as request  # To make HTTP requests
    from sys import argv  # To access command-line arguments

    # Creating a Request object with the URL passed as the first command-line
    # argument
    req = request.Request(argv[1])

    try:
        # Attempting to open the URL and read its contents
        with request.urlopen(req) as r:
            # Reading and decoding the response from bytes to a UTF-8 string
            print(r.read().decode('utf-8'))
    except error.HTTPError as e:
        # Catching an HTTPError if it occurs and printing the error code
        print("Error code: {}".format(e.code))
