#!/usr/bin/python3
"""sends request to a URL and display the response body"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    # Check if the status code indicates an error (>= 400)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
