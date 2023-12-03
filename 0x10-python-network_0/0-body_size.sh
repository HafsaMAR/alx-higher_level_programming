#!/bin/bash
#display the size of bytes
curl -sI "$1" | grep Content-Length | cut -d' ' -f2
