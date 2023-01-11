#!/usr/bin/python3
"""Task Answer"""
import json


def load_from_json_file(filename):
    """create py object form json file:)"""
    with open(filename, 'w+', encoding="utf-8") as f:
        return json.load(f)
