#!/usr/bin/python3
"""classgeo file"""


class BaseGeometry:
    """geometry class"""

    def area(self):
        raise Exception("area() is not implemented")
