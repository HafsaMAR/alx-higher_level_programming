#!/bin/bash
# Displays the size of the body
curl -sI "$1" | grep "Allow" | cut -d' ' -f 2-
