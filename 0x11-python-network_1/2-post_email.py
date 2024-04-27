#!/usr/bin/python3
""" POST request to a given URL with email"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email as ASCII
    data = urllib.parse.urlencode({"email": email}).encode("ascii")

    # Create a POST request object for specified URL with encoded email data
    request = urllib.request.Request(url, data)

    # Send the POST request and capture the response
    with urllib.request.urlopen(request) as response:
        # Decode and print the body of the response
        print(response.read().decode("utf-8"))
