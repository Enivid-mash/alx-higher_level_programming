#!/bin/bash
# takes a url, sends a POST request and displays response body 

curl --silent --request POST --data "email=test@gmail.com&subject=I will always be here for PLD" "$1"
