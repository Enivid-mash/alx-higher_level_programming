#!/bin/bash
# send a DELETE request to an URL with curl and display the body of the response
curl --silent --request DELETE "$1"
