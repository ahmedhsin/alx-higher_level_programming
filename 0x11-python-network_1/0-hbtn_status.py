#!/usr/bin/python3
"""script used for get content of website"""
import urllib.request


def main():
    """Start of the program"""
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        html = response.read()
    print("    - type: " + str(type(html)) + "$")
    print("    - content: " + str(html) + "$")
    print("    - utf8 content: " + html.decode() + "$")


""""
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
"""

if __name__ == "__main__":
    main()
