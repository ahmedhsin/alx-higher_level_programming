#!/usr/bin/python3
"""Task Answer"""
import json


def class_to_json(obj):
    """class to json"""

    return json.loads(json.dumps(obj.__dict__))
