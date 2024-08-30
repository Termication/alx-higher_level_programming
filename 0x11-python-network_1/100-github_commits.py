#!/usr/bin/python3
"""Script that fetches the last 10 commits from a given GitHub repository."""

import sys
import requests

if __name__ == "__main__":
    # Format the URL to access commits of a specified GitHub repository
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    # Send a GET request to the GitHub API
    r = requests.get(url)
    commits = r.json()

    try:
        # Loop through the first 10 commits and print their SHA and author name
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        # If there are fewer than 10 commits, exit gracefully
        pass
