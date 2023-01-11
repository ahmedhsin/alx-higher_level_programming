#!/usr/bin/python3

import sys

def main():
    del sys.argv[0]
    for i in sys.argv:
        print(i)

main()
