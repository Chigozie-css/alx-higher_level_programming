#!/bin/bash
# Displays all HTTP methods accepted by the server of the specified URL.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
