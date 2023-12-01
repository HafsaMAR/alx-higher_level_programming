#!/bin/bash
#take in URL as argument
url=$1

#Send request to URL and save response to body variable
response=$(curl -sI "$url" | awk '/Content-Length/ {print $2}' | tr -d '\r')

#Get size of response body bytes
size=$(echo -n "$response" | wc -c)

echo "$size"
