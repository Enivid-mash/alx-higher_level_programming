#!/usr/bin/python3
""" sends POST request to URL with an email and displays the response body"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {"email": email}
    response = requests.post(url, data=payload)
    print(response.text)
