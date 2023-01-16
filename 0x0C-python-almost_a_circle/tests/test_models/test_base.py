#!/usr/bin/python3
"""base class unittest"""
import sys

#sys.path.append(
#    "/home/yuu/alx-higher_level_programming/0x0C-python-almost_a_circle/")
import unittest
from models.base import *
from models.rectangle import Rectangle


class Test_Base(unittest.TestCase):
    """test class"""

    def test_object(self):
        """test_object"""
        Base._Base__nb_objects = 0
        obj = Base()
        self.assertEqual(obj.id, 1)
        obj = Base()
        self.assertEqual(obj.id, 2)
        obj = Base(10)
        self.assertEqual(obj.id, 10)

    def test_to_json(self):
        """test_to_json"""
        dictionary = {"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}
        s = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test__save_tofile(self):
        """save_to_file"""
        ans = '[{"x": 8, "y": 2, "id": 111, "height": 7, "width": 10}, '
        ans2 = '{"x": 1, "y": 1, "id": 11, "height": 7, "width": 10}]'
        Rectangle.save_to_file(
            [Rectangle(10, 7, 8, 2, 111), Rectangle(10, 7, 1, 1, 11)]
        )
        with open("Rectangle.json", "r", encoding="utf-8") as f:
            data = f.read()
        self.assertEqual(data, ans + ans2)
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="utf-8") as f:
            data = f.read()
        self.assertEqual(data, "[]")

    def test_from_json(self):
        """test_from_json"""
        list_input = [
            {"id": 89, "width": 10, "height": 4},
            {"id": 7, "width": 1, "height": 7},
        ]
        int_input = [5, 6, 7, 8]
        json_str = Base.to_json_string(list_input)
        self.assertEqual(Base.from_json_string(json_str), list_input)
        json_str = Base.to_json_string(int_input)
        self.assertEqual(Base.from_json_string(json_str), int_input)

    def test_create(self):
        """test create"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(r1 == r2, False)
        self.assertEqual(r1 is r2, False)

    def test_load_fromfile(self):
        """test load"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        objects = Rectangle.load_from_file()

        self.assertEqual(objects[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(objects[1].to_dictionary(), r2.to_dictionary())



if __name__ == "__main__":
    unittest.main()
