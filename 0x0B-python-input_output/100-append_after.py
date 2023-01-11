#!/usr/bin/python3
"""Task Answer"""


def append_after(filename="", search_string="", new_string=""):
    index = []
    cnt = 1
    lines = None
    with open(filename, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    for i in lines:
        if search_string in i:
            index.append(cnt)
        cnt += 1
    for i in index:
        lines.insert(i, new_string)
    with open(filename, 'w', encoding="utf-8") as f:
        for i in lines:
            f.write(i + '\n')
