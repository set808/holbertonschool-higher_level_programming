#!/usr/bin/python3


def args(argv):
    arg_num = len(argv) - 1

    if len(argv) > 2:
        print('{:d} arguments:'.format(arg_num))
    elif len(argv) == 1:
        print('{:d} arguments.'.format(arg_num))
    else:
        print('{:d} argument:'.format(arg_num))

    for i, arg in enumerate(argv[1:], 1):
            print("{:d}: {:s}".format(i, arg))

if __name__ == "__main__":
    import sys
    args(sys.argv)
