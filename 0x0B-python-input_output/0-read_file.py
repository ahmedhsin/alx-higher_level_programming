#!/usr/bin/python3
"""Task Answer"""


def read_file(filename=""):
    """Read from file func"""
    with open(filename, encoding="utf-8") as f:
        data = f.read()
        print(data, end="")
