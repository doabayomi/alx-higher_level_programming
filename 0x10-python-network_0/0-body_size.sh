#!/bin/bash
# Getting the Content-Size of the HTTP request
curl -s -I $1 | grep "Content-Length" | awk '{print $2}'
