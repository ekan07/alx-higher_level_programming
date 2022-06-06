#!/usr/bin/python
def divisible_by_2(my_list=[]):
    l_itm = []
    for i in range(len(my_list)):
        itm = True if my_list[i] % 2 == 0 else False
        l_itm.append(itm)
    return l_itm
