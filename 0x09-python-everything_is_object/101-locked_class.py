#!/usr/bin/python3
class LockedClass:
    err = "'LockedClass' object has no attribute 'last_name'"

    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError(err)
