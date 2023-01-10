#!/usr/bin/python3
"""classgeo file"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ovrride str fun"""
        return "[Square] {}/{}".format(self.__size, self.__size)
