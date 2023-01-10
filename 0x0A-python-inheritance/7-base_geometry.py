#!/usr/bin/python3
"""classgeo file"""


class BaseGeometry:
    """geometry class"""

    def area(self):
        """area fun"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """intger validator"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
