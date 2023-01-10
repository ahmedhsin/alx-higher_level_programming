#!/usr/bin/python3
"""func file"""


def inherits_from(obj, a_class):
    """check if obj is instance of specif class"""

    if type(obj) != a_class and isinstance(obj, a_class):
        return True
    else:
        return False
