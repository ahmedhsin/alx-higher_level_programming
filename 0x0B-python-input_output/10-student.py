#!/usr/bin/python3
"""Task Answer"""


class Student:
    """Student Class"""
    first_name = None
    last_name = None
    age = None

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            nnw = attrs.copy()
            nnw.sort()
            data = {}
            for i in nnw:
                try:
                    data[i] = self.__dict__[i]
                except Exception:
                    pass
        return data
