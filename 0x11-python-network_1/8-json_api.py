#!/usr/bin/python3
"""script used for header token website"""
import requests
import sys


def main():
    """Start of the program"""
    q = ""
    try:
        q = sys.argv[1]
    except Exception:
        pass
    try:
        r = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
        content = r.json()
        if (len(content) == 0):
            print("No result")
        else:
            print("[{}] {}".format(content["id"], content["name"]))
    except Exception:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
