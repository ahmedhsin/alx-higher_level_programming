#!/usr/bin/python3
"""Advanced Task"""


class MyInt(int):
    """class"""
    def __eq__(self, other):
        """overload equ"""
        return super().__ne__(other)

    def __ne__(self, other):
        """overlaod nequ"""
        return super().__eq__(other)
