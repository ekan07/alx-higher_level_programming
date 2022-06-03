#!/usr/bin/python3
def print_arg(argv):
    arg_len = len(argv) - 1
    if arg_len == 1:
        print("{:d} argument:".format(arg_len))
    else:
        print("{:d} arguments:".format(arg_len))
    i = 1
    while i <= arg_len:
        print("{:d}: {:s}".format(i, argv[i]))
        i += 1


if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
