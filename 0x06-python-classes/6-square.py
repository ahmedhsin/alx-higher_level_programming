#!/usr/bin/python3
"""Define a class called Square"""


class Square:
    """Represent of Square class
        Attributes:
           __size (int): size of square
    """
    def __init__(self, size=0, position=(0, 0)):
        """initialize instance
            Args:
                self (object<Square>): mandatory arg in python
                size (int): size of square default value is 0
                position (tuple): position of
                square on cordinate default value (0,0)
            Return:
                nothing
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """return current x when called by dot operator"""
        return self.__size

    @size.setter
    def size(self, size):
        """set x when called by dot operator"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """return position"""
        return self.__position

    @position.setter
    def position(self, position):
        """set position and some constraint"""
        instance = isinstance(position, tuple)
        length = len(position)
        if not instance or length != 2 or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """ Method area
            Args:
                self (square): referre to object
            Return:
                square area
        """
        Area = self.__size * self.__size
        return Area

    def my_print(self):
        """function draw the square in stdout
            Args:
                self (square): refree to obj
            Return:
                void
        """
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
