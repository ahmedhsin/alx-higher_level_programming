#!/usr/bin/python3
import json
"""Task Answer"""


def to_json_string(my_obj):
    """json to object"""
    return json.dumps(my_obj, sort_keys=True)
