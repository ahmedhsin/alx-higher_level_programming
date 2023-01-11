#!/usr/bin/python3
import json
"""Task Answer"""


def from_json_string(my_str):
    """json to object"""
    return json.loads(my_str, sort_keys=True)
