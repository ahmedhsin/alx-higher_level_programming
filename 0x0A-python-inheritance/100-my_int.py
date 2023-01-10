#!/usr/bin/python3
"""Advanced Task"""

class MyInt(int):
    def __init__(self, x):
        if (type(x) != int):
            raise TypeError
        self.__ans = x

    def __str__(self):
        """overload str"""
        return "{}".format(self.__ans)

    def __eq__(self, other):
        """overload equ"""
        return not (self.__ans == other)

    def __ne__(self, other):
        """overlaod nequ"""
        return (self.__ans == other)
