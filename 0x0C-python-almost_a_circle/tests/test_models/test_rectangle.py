#!/usr/bin/python3
"""Rectangle class unittest"""
import sys

#sys.path.append(
#    "/home/yuu/alx-higher_level_programming/0x0C-python-almost_a_circle/")
import unittest
from models.rectangle import Rectangle


class Test_Base(unittest.TestCase):
    """test class"""

    def test_validtion(self):
        """test definition"""
        with self.assertRaises(ValueError):
            Rectangle(0, 1, 0, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 0, 0, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 0, -1)

        with self.assertRaises(TypeError):
            Rectangle("lol", 1, 1, 1)
        with self.assertRaises(TypeError):
            Rectangle(1, "lol", 1, 1)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, None, 1)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, "Lol")
        with self.assertRaises(TypeError):
            Rectangle(1, None, 1, 1)

    def test_area(self):
        """test definition"""
        self.assertEqual(Rectangle(5, 9, 1, 1).area(), 5 * 9)
        self.assertEqual(Rectangle(2, 3, 1, 1).area(), 2 * 3)

    def test_str(self):
        self.assertEqual(
            str(Rectangle(5, 9, 0, 1, 78)), "[Rectangle] (78) 0/1 - 5/9")
        self.assertEqual(
            str(Rectangle(2, 2, 0, 0, 99)), "[Rectangle] (99) 0/0 - 2/2")

    def test_update(self):
        """test definition"""
        obj = Rectangle(5, 6, 1, 0, 5)
        obj.update(1)
        self.assertEqual(obj.id, 1)
        obj.update(1, 2)
        self.assertEqual(obj.width, 2)
        obj.update(1, 2, 3)
        self.assertEqual(obj.height, 3)
        obj.update(1, 2, 3, 4)
        self.assertEqual(obj.x, 4)
        obj.update(1, 2, 3, 4, 5)
        self.assertEqual(obj.y, 5)

        obj.update(id=7)
        self.assertEqual(obj.id, 7)
        obj.update(width=8, height=9)
        self.assertEqual(obj.width + obj.height, 8 + 9)
        obj.update(y=9, x=17)
        self.assertEqual(obj.y + obj.x, 9 + 17)
        with self.assertRaises(TypeError):
            obj.update(width=3.5)

    def test_dict(self):
        """test definition"""
        obj = Rectangle(10, 2, 1, 9, 1)
        d1 = {"x": 1, "y": 9, "id": 1, "height": 2, "width": 10}
        d2 = {"x": 1, "y": 9, "id": 8, "height": 7, "width": 13}
        self.assertEqual(
            obj.to_dictionary(), d1
        )
        obj = Rectangle(13, 7, 1, 9, 8)
        self.assertEqual(
            obj.to_dictionary(), d2
        )
        self.assertEqual(type(obj.to_dictionary()), dict)


"""
        valid till now
        obj = Rectangle(1,1,1,1)
        obj.update(lol=15)
        self.assertEqual(obj.lol, 15)
"""

if __name__ == "__main__":
    unittest.main()
