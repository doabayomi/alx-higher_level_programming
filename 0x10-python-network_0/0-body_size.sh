#!/usr/bin/bash
# Getting the Content-Size of the HTTP request
curl -Is $1 | grep "Content-Length" | awk '{print $2}'
