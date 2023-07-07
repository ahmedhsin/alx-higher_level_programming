#!/usr/bin/python3
"""script used for header token website"""
import requests
import sys


def main():
    """Start of the program"""
    url = sys.argv[1]
    r = requests.get(url)
    if (r.status_code >= 400):
        print("Error code: " + str(r.status_code))
    else:
        print(r.text)


if __name__ == "__main__":
    main()
