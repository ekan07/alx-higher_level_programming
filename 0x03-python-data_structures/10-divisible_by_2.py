#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    l_itm = []
    for i, _ in enumerate(my_list):
        itm = True if my_list[i] % 2 == 0 else False
        l_itm.append(itm)
    return l_itm
