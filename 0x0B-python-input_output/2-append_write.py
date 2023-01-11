#!/usr/bin/python3
"""Task Answer"""


def append_write(filename="", text=""):
    """Append from file func"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
