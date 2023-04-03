#!/bin/bash
#post
curl -sX POST "$1" -d @"$2" -H "Content-Type: application/json"
