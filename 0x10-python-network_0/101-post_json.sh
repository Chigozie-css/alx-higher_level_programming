#!/bin/bash
# Sends a JSON POST request with file data to a URL.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
