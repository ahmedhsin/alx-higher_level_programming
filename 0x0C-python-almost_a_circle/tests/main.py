#1/usr/bin/python3
import sys
sys.path.append('/home/yuu/alx-higher_level_programming/0x0C-python-almost_a_circle/')
from models.square import Square, Rectangle
from models.base import Base
def main():
    s1 = Square(5)
    print(s1)

    s1.update(10)
    print(s1)

    s1.update(1, 2)
    print(s1)

    s1.update(1, 2, 3)
    print(s1)

    s1.update(1, 2, 3, 4)
    print(s1)

    s1.update(x=12)
    print(s1)

    s1.update(size=7, y=1)
    print(s1)

    s1.update(size=7, id=89, y=1)
    print(s1)
