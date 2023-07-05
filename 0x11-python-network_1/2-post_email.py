#!/usr/bin/python3
"""script used for send email to a website"""
import urllib.request
import sys


def main():
    """Start of the program"""
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode())


if __name__ == "__main__":
    main()
