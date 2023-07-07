#!/usr/bin/python3
"""script used for get coent website"""
import requests


def main():
    """Start of the program"""
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("- type: " + str(type(r.text)))
    print("- content: " + r.text)


if __name__ == "__main__":
    main()
