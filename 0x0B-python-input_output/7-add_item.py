#!/usr/bin/python3
"""Task Answer"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """script for add/rem"""

    path = "add_item.json"
    obj = load_from_json_file(path)
    with open(path, 'w+', encoding="utf-8") as f:
        del sys.argv[0]
        for i in sys.argv:
            obj.append(i)

main()
