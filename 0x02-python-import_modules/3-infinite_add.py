#!/usr/bin/python3


def infinite_add(argv):
    result = 0
    for i, num in enumerate(argv[1:]):
        result += int(num)
    print("{:d}".format(result))

if __name__ == '__main__':
    import sys
    infinite_add(sys.argv)
