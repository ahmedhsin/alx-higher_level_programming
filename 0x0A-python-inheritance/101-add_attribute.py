#!/usr/bin/python3
"""adv function blabla"""


def add_attribute(obj, name, value):
    """func to ADD atrr blasvlas"""

    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
