#!/usr/bin/python3
""" sends a request to a given URL and displays the response body"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]

    # Create a request object for the specified URL
    request = urllib.request.Request(url)

    try:
        # Send the request and capture the response
        with urllib.request.urlopen(request) as response:
            # Decode and print the body of the response
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        # Handle HTTP errors by printing the error code
        print("Error code: {}".format(e.code))
