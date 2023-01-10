#!/usr/bin/python3
"""func file"""


def is_same_class(obj, a_class):
    """check if obj is instance of specif class"""
    try:
        if (isinstance(obj, a_class)):
            return True
        else:
            return False
    except Exception:
        return False
