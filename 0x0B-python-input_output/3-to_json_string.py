#!/usr/bin/python3
import json
"""Task Answer"""


def to_json_string(my_obj):
    """json to object"""
    data = json.dumps(my_obj, sort_keys=True)
    return data
