#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # re_itm = replace if el == search else el
    res = [el if el != search else replace for el in my_list]
    return res
