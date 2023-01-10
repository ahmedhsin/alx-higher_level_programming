#!/usr/bin/python3
"""adv class"""


def add_attribute(obj, name, value):
    if hasattr(obj, '__dict__') not True:
        raise TypeError("can't add new attribute")
    obj.__dict__[name] = value
