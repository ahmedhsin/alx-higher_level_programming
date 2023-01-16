#!/usr/bin/python3
"""Rectangle Class"""
from .base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def check_intger(self, name, obj):
        """Valdiate function"""
        if type(obj) != int:
            raise TypeError("{} must be an integer".format(name))

    def lt_zero(self, name, obj):
        """Valdiate function"""
        if obj <= 0:
            raise ValueError("{} must be > 0".format(name))

    def le_zero(self, name, obj):
        """Valdiate function"""
        if obj < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.check_intger("width", width)
        self.lt_zero("width", width)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.check_intger("height", height)
        self.lt_zero("height", height)
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.check_intger("x", x)
        self.le_zero("x", x)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.check_intger("y", y)
        self.le_zero("y", y)
        self.__y = y

    def area(self):
        """calculate area"""
        return self.__width * self.__height

    def display(self):
        """Print on screen"""
        print('\n' * self.y, end="")
        for i in range(self.__height):
            print(" " * self.x, end="")
            print("{}".format(self.__width * "#"))

    def __str__(self):
        """override str"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **keyargs):
        """update method"""
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except Exception:
            pass
        for key, value in keyargs.items():
            # if key in self.__dict__ or key in super().__dict__:
            setattr(self, key, value)

    def to_dictionary(self):
        """to dict"""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width,
        }
