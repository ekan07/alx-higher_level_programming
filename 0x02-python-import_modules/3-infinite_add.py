#!/usr/bin/python3
def add_args(argv):
    res = 0
    for i in range(1, len(argv)):
        res += int(argv[i])
    print("{:d}".format(res))

if __name__ == "__main__":
    import sys
    add_args(sys.argv)
