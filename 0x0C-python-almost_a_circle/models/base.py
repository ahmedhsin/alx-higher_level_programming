#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Base Class"""

import json


class Base:

    """Base Class specifi"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json function"""
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file"""
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as file:
            dictionaries = []
            if list_objs is None:
                pass
            else:
                for i in list_objs:
                    dictionaries.append(i.to_dictionary())
                data = Base.to_json_string(dictionaries)
                file.write(data)

    def from_json_string(json_string):
        """from_json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create object"""
        dummyobject = cls(3, 5, 1, 0, 1)
        dummyobject.update(**dictionary)
        return dummyobject

    @classmethod
    def load_from_file(cls):
        """load from file"""
        objects_list = []
        try:
            filename = cls.__name__ + '.json'
            with open(filename, 'r', encoding='utf-8') as file:
                dictionary_list = json.load(file)
                for i in dictionary_list:
                    objects_list.append(cls.create(**i))
        except Exception:
            pass

        finally:
            return objects_list