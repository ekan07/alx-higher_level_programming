#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    res = list(map(lambda a: number * a, my_list))
    return res

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)