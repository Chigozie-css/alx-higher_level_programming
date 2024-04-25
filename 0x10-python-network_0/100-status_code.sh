#!/bin/bash
# Sends a request to the specified URL and shows only the status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
