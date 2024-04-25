#!/bash/bash
# Sends a request to a URL passed as an argument and displays only the status code of the response.

curl -s -o tmp_response.txt -w "%{http_code}" "$1"
cat tmp_response.txt
rm tmp_response.txt
