#!/usr/bin/python3
"""script used for header token website"""
import requests
import sys


def main():
    """Start of the program"""
    url = sys.argv[1]
    r = requests.post(url, data={"email": sys.argv[2]})
    print(r.text)


if __name__ == "__main__":
    main()
