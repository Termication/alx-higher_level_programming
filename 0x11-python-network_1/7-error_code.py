#!/usr/bin/python3
"""
This script makes an HTTP GET request to a URL
specified as a command-line argument.
It uses the `requests` library to handle
the HTTP request and response.
If the HTTP status code is 400 or higher,
indicating an error, the script prints an error
message with the status code.
If the request is successful (status code less than 400),
the script prints the response content.
"""

if __name__ == '__main__':
    import requests  # To make HTTP requests easily
    from sys import argv  # To access command-line arguments

    # Sending an HTTP GET request to the URL provided as the first
    # command-line argument
    r = requests.get(argv[1])

    # Checking if the HTTP status code indicates an error (status codes 400
    # and above)
    if r.status_code >= 400:
        # If there is an error, print the status code with an error message
        print("Error code: {}".format(r.status_code))
    else:
        # If the request is successful, print the content of the response
        print(r.text)
