#!/usr/bin/python3
"""
This script fetches the status from https://alx-intranet.hbtn.io/status
and displays the body response in a formatted manner.
"""

if __name__ == "__main__":
    import urllib.request as request

    # Fetch the URL
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()

        # Print the body response details
        print('Body response:')
        # Print the type of the response content
        print("\t- type: {}".format(type(html)))
        # Print the raw content of the response
        print("\t- content: {}".format(html))
        # Print the decoded (UTF-8) content of the response
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
