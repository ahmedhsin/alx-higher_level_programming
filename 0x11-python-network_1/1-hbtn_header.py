#!/usr/bin/python3
"""script used for get header of website"""
import urllib.request
import sys


def main():
    """Start of the program"""
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.getheader("X-Request-Id"))


if __name__ == "__main__":
    main()
