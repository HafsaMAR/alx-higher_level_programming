#!/bin/bash
#take in URL as argument
url=$1

#Send request to URL and save response to body variable
curl -sI "$url" | grep Content-Length | cut -d' ' -f2


