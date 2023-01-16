#!/usr/bin/python3
"""Square File"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        """str override"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **keyargs):
        """update"""
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except Exception:
            pass
        for key, value in keyargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """to dict override"""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
