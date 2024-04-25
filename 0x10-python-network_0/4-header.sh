#!/bin/bash
# Sends a GET request to the specified URL with a custom header variable.
curl -sH "X-HolbertonSchool-User-Id: 98" "${1}"
