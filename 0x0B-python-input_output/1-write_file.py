#!/usr/bin/python3
"""Task Answer"""


def write_file(filename="", text=""):
    """Write from file func"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
