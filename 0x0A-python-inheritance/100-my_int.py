#!/usr/bin/python3
"""Advanced Task"""


class MyInt(int):
    """class"""
    def __eq__(self, other):
        """overload equ"""
        return not (super() == other)

    def __ne__(self, other):
        """overlaod nequ"""
        return (super() == other)
