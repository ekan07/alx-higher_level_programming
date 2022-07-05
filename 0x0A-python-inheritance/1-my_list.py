#!/usr/bin/python3
"""
Module 1-my_list
"""

class MyList(list):
    """MyList that inherits from list"""
    def print_sorted(self):
        """print_sorted print sorted list"""
        res = self[:]
        print("{}".format(sorted(res)))
