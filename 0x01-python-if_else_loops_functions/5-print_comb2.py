#!/usr/bin/python3
strs = ', '
for i in range(100):
    if i < 10:
        print(f"0{i}", end=', ')
    else:
        if i == 99:
            strs = '\n'
        print(f"{i}", end=strs)
