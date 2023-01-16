#!/usr/bin/python3
"""Square class unittest"""
import sys

sys.path.append(
    "/home/yuu/alx-higher_level_programming/0x0C-python-almost_a_circle/")
import unittest
from models.square import Square
from models.base import Base


class Test_Base(unittest.TestCase):
    """test class"""

    def test_validtion(self):
        """test definition"""
        with self.assertRaises(ValueError):
            Square(0, 0, 0)
        with self.assertRaises(ValueError):
            Square(1, -1, 0)
        with self.assertRaises(ValueError):
            Square(1, 1, -1)

        with self.assertRaises(TypeError):
            Square("lol", 1, 1)
        with self.assertRaises(TypeError):
            Square(1, "lol", 1)
        with self.assertRaises(TypeError):
            Square(1, None, 1)
        with self.assertRaises(TypeError):
            Square(1, 1, "Lol")
        with self.assertRaises(TypeError):
            Square(1, None, 1)

    def test_area(self):
        """test definition"""
        self.assertEqual(Square(5, 1, 1).area(), 5 * 5)
        self.assertEqual(Square(2, 1, 1).area(), 2 * 2)

    def test_str(self):
        """test definition"""
        self.assertEqual(
            Square(5, 0, 1, 78).__str__(), "[Square] (78) 0/1 - 5")
        self.assertEqual(
            Square(2, 0, 0, 99).__str__(), "[Square] (99) 0/0 - 2")

    def test_size(self):
        """test definition"""
        obj = Square(5, 2, 4)
        self.assertEqual(obj.size, obj.width)
        self.assertEqual(obj.size, obj.height)
        obj.size = 4
        self.assertEqual(obj.size, obj.width)
        self.assertEqual(obj.size, obj.height)

    def test_update(self):
        """test definition"""
        obj = Square(5, 6, 0, 5)
        obj.update(1)
        self.assertEqual(obj.id, 1)
        obj.update(1, 2)
        self.assertEqual(obj.width, 2)
        obj.update(1, 2, 3)
        self.assertEqual(obj.height, 2)
        obj.update(1, 2, 4)

        obj.update(id=7)
        self.assertEqual(obj.id, 7)
        obj.update(y=9, x=17)
        self.assertEqual(obj.y + obj.x, 9 + 17)
        with self.assertRaises(TypeError):
            obj.update(width=3.5)
        obj.update(size=7)
        self.assertEqual(obj.size, 7)
        self.assertEqual(obj.width + obj.height, 7 + 7)
        obj.update(y=9, x=17)
        self.assertEqual(obj.y + obj.x, 9 + 17)
        with self.assertRaises(TypeError):
            obj.update(size=3.5)

    def test_dict(self):
        """test definition"""
        obj = Square(10, 2, 1, 1)
        self.assertEqual(
            obj.to_dictionary(), {"id": 1, "x": 2, "size": 10, "y": 1})
        obj.update(x=3, size=15)
        self.assertEqual(
            obj.to_dictionary(), {"id": 1, "x": 3, "size": 15, "y": 1})
        self.assertEqual(type(obj.to_dictionary()), dict)


if __name__ == "__main__":
    unittest.main()
