#!/usr/bin/python3
"""Task Answer"""
import json


def save_to_json_file(my_obj, filename):
    """json to object"""
    with open(filename, 'a', encoding="utf-8") as f:
        return json.dump(my_obj, f, sort_keys=True)
