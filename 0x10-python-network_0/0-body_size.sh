#!/bin/bash
# takes a url, sends request and displays response size
curl --silent "$1" | wc -c
