#!/usr/bin/python3
strs = ', '
for i in range(100):
    if i < 10:
        print("0{}".format(i), end=', ')
    else:
        if i == 99:
            strs = '\n'
        print("{}".format(i), end=strs)
