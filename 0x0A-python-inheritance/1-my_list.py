#!/usr/bin/python3
##################
"""Class My list"""
##################


class MyList(list):
    """my class inhert from list class"""
    def print_sorted(self):
        """method for copy a list then sort it and print it"""
        sr_list = self[:]
        sr_list.sort()
        print(sr_list)
