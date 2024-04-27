#!/usr/bin/python3
""" displays the X-Request-Id header variable of a request to a URL"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    print(response.headers.get("X-Request-Id"))
