#!/usr/bin/python3
"""func file"""


def is_same_class(obj, a_class):
    """check if obj is instance of specif class"""

    try:
        state = isinstance(obj, a_class)
    except TypeError:
        try:
            state = isinstance(a_class, obj)
        except Exception:
            state = False
    except Exception:
        state = False

    if (state):
        return True
    else:
        return False
