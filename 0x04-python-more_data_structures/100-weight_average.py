#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    res, s1 = 0, 0
    for x, y in my_list:
        res += (x * y)
        s1 += y
    return (res / s1)
