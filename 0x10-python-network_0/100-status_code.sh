#!/bin/bash
# Getting the status code of a response
curl -w "%{http_code}" -I -s -o /dev/null $1
