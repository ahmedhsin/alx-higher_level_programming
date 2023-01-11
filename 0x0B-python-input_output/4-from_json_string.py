#!/usr/bin/python3
import json
"""Task Answer"""


def from_json_string(my_str):
    """json to object"""
    data = json.loads(my_str, sort_keys=True)
    return data
