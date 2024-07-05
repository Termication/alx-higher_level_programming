#!/usr/bin/python3
"""
This script fetches the status from https://alx-intranet.hbtn.io/status
using the requests package and displays the body response.
"""

if __name__ == '__main__':
    import requests

    # Send a GET request to the specified URL
    response = requests.get('https://alx-intranet.hbtn.io/status')
    text = response.text

    # Print the body response details
    print("Body response:")
    print("\t- type: {}".format(type(text)))  # Print the type of the response content
    print("\t- content: {}".format(text))     # Print the content of the response
