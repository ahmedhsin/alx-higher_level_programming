#!/usr/bin/python3
"""Task Answer"""
import json


def to_json_string(my_obj):
    """json to object"""
    return json.dumps(my_obj, sort_keys=True)
