#!/bin/bash
# Gettting allowed HTTP methods acceptable to the server
curl -s -I $1 | grep -oP 'Allow: \K.*'
