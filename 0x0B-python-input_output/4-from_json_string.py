#!/usr/bin/python3
import json
"""Task Answer"""


def from_json_string(my_str):
    """Json To obj fun"""
    return json.loads(my_str, sort_keys=True)
