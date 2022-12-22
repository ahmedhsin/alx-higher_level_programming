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
        self.size = size

    @property
    def size(self):
        """return current x when called by dot operator"""
        return self.__size

    @size.setter
    def size(self, size):
        """set x when called by dot operator"""
        if not isinstance(size, int) and not isinstance(size, float):
            raise TypeError("size must be a number")
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

    def __eq__(self, other):
        """equality method override"""
        if isinstance(other, Square):
            return self.size == other.size
        return False

    def __ne__(self, other):
        """not equality method"""
        return not self.__eq__(other)

    def __gt__(self, other):
        """greater than method"""
        if isinstance(other, Square):
            return self.size > other.size
        return False

    def __lt__(self, other):
        """less than method"""
        if isinstance(other, Square):
            return self.size < other.size
        return False

    def __ge__(self, other):
        """greater or equal"""
        if isinstance(other, Square):
            return self.size > other.size or self.__eq__(other)
        return False

    def __le__(self, other):
        """less than or equal"""
        if isinstance(other, Square):
            return self.size < other.size or self.__eq__(other)
        return False
