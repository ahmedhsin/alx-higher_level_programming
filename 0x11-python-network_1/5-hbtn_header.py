#!/usr/bin/python3
"""script used for header token website"""
import requests
import sys


def main():
    """Start of the program"""
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers["X-Request-Id"])


if __name__ == "__main__":
    main()
