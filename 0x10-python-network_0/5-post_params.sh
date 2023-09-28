#!/bin/bash
# Sending a POST request in bash
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST $1
