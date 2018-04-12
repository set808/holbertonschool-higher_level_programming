#!/usr/bin/python3


def args(argv):
    if len(argv) > 2 or len(argv) == 1:
        print('{:d} arguments:'.format(len(argv) - 1))
    else:
        print('{:d} argument:'.format(len(argv) - 1))

    for i, arg in enumerate(argv[1:], 1):
            print("{:d}: {:s}".format(i, arg))

if __name__ == "__main__":
    import sys
    args(sys.argv)
