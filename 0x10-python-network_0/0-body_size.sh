#!/bin/bash
#Content Length
curl -sI "$1" | grep "Content-Length" | grep -E -o '[0-9]+'
