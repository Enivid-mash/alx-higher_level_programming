#!/bin/bash
# request to the URL, and display the body of the response

curl --silent --header "X-School-User-Id: 98" "$1"
