#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as err:
        sys.stderr.write("Exception: {}\n".format(err))
        # print("Exception: {}".format(err), file=sys.stderr)
        return False
