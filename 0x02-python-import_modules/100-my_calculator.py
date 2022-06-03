#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def calculate(argv):
    n = len(argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a, b, opr = int(argv[1]), int(argv[3]), argv[2]
    if opr == '+':
        print("{:d} {:s} {:d} = {:d}".format(a, opr, b, add(a, b)))
    elif opr == '-':
        print("{:d} {:s} {:d} = {:d}".format(a, opr, b, sub(a, b)))
    elif opr == '*':
        print("{:d} {:s} {:d} = {:d}".format(a, opr, b, mul(a, b)))
    elif opr == '/':
        print("{:d} {:s} {:d} = {:d}".format(a, opr, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, *, /")
        exit(1)


if __name__ == "__main__":
    import sys
    calculate(sys.argv)
  