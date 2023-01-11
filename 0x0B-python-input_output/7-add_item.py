#!/usr/bin/python3
"""Task Answer"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """script for add/rem"""

    path = "add_item.json"
    try:
        obj = load_from_json_file(path)
    except Exception:
        obj = []

    del sys.argv[0]
    for i in sys.argv:
        obj.append(i)
    save_to_json_file(path, f)


main()
