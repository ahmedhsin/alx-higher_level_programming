#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return (str)
    else:
        strr = ""
        for i in range(len(str)):
            if i != n:
                strr = strr + str[i]
    return (strr)
