#!/usr/bin/python3
def discover(hidden):
    names = dir(hidden)
    for i in names:
        if i[:2] != "__":
            print("{:s}".format(i))


if __name__ == "__main__":
    import hidden_4
    discover(hidden_4)
