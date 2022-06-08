#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    res = a_dictionary.copy()
    res = {k: 2 * res[k] for k in res}
    return res
