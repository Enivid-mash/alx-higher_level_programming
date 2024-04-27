#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    # Create a request object for the specified URL
    request = urllib.request.Request(url)

    # Send the request and capture the response
    with urllib.request.urlopen(request) as response:
        # Retrieve the HTTP headers from the response
        headers = dict(response.headers)
        # Extract and print the value of the X-Request-Id header
        x_request_id = headers.get("X-Request-Id")
        print(x_request_id)
