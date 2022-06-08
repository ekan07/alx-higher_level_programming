#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    s = sorted(a_dictionary, key=lambda a: a_dictionary.get(a), reverse=True)
    return s[0]
    