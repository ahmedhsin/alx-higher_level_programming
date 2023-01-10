#!/usr/bin/python3
"""adv function blabla"""


def add_attribute(obj, name, value):
    """func to ADD atrr blasvlas"""

    if hasattr(obj, '__dict__') not True:
        raise TypeError("can't add new attribute")
    obj.__dict__[name] = value
