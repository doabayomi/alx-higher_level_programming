#!/bin/bash
# Sending a post request using a json file
curl -s -H "Content-Type: application/json" -d '$(cat "$2")' -X POST $1
