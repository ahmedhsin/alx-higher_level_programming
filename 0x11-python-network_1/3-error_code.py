#!/usr/bin/python3
"""script used for handel error website"""
import urllib.request
import sys


def main():
    """Start of the program"""
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode())
    except urllib.error.HTTPError as e:
        print("Error code: " + str())


if __name__ == "__main__":
    main()
