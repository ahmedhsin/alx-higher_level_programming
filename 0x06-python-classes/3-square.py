#!/usr/bin/python3
"""Define a class called Square"""


class Square:
    """Represent of Square class
        Attributes:
           __size (int): size of square
    """
    def __init__(self, size=0):
        """initialize instance
            Args:
                self (object<Square>): mandatory arg in python
                size (int): size of square default value is 0
            Return:
                nothing
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Method area
            Args:
                self (square): referre to object
            Return:
                square area
        """
        Area = self.__size * self.__size
        return Area
