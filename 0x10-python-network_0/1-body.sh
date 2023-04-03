#!/bin/bash
#get content if OK
STATE=$(curl -sI "$1" | grep '200 OK' | grep -c -E '[0-9]+')
if [ "$STATE" -eq 1 ]; then
	curl -s "$1"
fi
