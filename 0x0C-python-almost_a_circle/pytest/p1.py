#!/usr/bin/python3
import unittest


class Test_Component(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(5+5, 10)

if __name__ == "__main__":
    unittest.main()
