#!/usr/bin/python3
"""Module 7-add_item.
Adds all arguments to a Python list,
and then save them to a file.
"""
import sys
import json
import os.path

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

num = len(sys.argv)


try:
    data = load_from_json_file('add_item.json')
except:
    data = []

for i in range(1, num):
    data.append(sys.argv[i])
save_to_json_file(data, 'add_item.json')
