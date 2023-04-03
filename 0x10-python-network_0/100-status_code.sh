#!/bin/bash
#state code
curl -sw "%{http_code}" -o /dev/null "$1"
