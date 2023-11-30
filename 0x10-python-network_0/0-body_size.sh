#!/bin/bash
# this script takes in a URL, sends a request to tthat URL, displays he size of the body of response
# the size is displayed in bytes
# te script uses curl to send the request

# check if the url is provided as argument
if [ $# -eq 0 ]; then
	echo "Usage: $0 url"
	exit 1
fi

# assigh the url to variable
url=$1

# Use curl to send a request to the URL and get the size of the body
# The -s option suppresses the progress meter
# The -w option writes the output to a format string
# The %{size_download} variable contains the size of the downloaded data in bytes
# The -o option redirects the output to /dev/null
size=$(curl -s -w "%{size_download}" -o /dev/null "$url")

# Display the size
echo "$size"
