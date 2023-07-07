#!/usr/bin/python3
"""script used for header token website"""
import requests
import sys


def main():
    """Start of the program"""
    header = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer {}".format(sys.argv[2]),
        "X-GitHub-Api-Version": "2022-11-28"
    }
    url = "https://api.github.com/users/{}".format(sys.argv[1])
    try:
        r = requests.get(url, headers=header)
        content = r.json()
        print("{}".format(content["id"]))
    except Exception:
        print("None")


if __name__ == "__main__":
    main()
