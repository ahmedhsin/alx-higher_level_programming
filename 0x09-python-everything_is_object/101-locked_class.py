#!/usr/bin/python3
"""
    locked class
"""
class LockedClass:
    """just class"""
    def __setattr__(self, name, value):
        """built in method"""
        if name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '" + name + "'")
