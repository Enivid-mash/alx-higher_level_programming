#!/bin/bash
# displays HTTP methods the server accepts
curl --silent --head "$1" | grep "Allow" | cut -d " " -f 2-
