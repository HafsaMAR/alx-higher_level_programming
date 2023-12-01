#!/bin/bash
#diplays body response (header varable)
curl -sX GET -H "X-School-User-Id: 98" "$1"
