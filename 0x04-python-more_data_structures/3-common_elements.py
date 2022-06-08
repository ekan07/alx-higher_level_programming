#!/usr/bin/python3
def common_elements(set_1, set_2):
    for tup in zip(set_1, set_2):
        if tup[0] == tup[1]:
            return tup[0]
