#!/usr/bin/python3
"""classgeo file"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """override area fun"""
        return self.__width * self.__height

    def __str__(self):
        """override str method"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
