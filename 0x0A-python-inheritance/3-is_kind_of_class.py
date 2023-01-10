#!/usr/bin/python3
"""func file"""


def is_kind_of_class(obj, a_class):
    """check if obj is instance of specif class"""

    if (isinstance(obj, a_class)):
        return True
    else:
        return False
