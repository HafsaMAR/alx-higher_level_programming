#!/bin/bash
#take in URL as argument
url=$1

#Send request to URL and save response to body variable
response=$(curl -s $url)

#Get size of response body bytes
size=$(echo -n "$response" | wc -c)

echo "$size"
