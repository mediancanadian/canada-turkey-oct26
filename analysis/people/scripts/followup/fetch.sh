#!/bin/bash
# usage: fetch.sh URL OUT
UA="Mozilla/5.0 (X11; Linux x86_64)"
for i in 1 2 3 4 5 6; do curl -sS -m 60 -A "$UA" -L "$1" -o "$2" -w "%{http_code} %{size_download} $1\n" 2>/dev/null && [ -s "$2" ] && exit 0; sleep 2; done; echo "FAIL $1"
