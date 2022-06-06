#!/usr/bin/python3
def multiple_returns(sentenc):
    str_len = len(sentenc)
    str_tuple = str_len, sentenc[0] if str_len > 0 else 'None'
    return str_tuple
