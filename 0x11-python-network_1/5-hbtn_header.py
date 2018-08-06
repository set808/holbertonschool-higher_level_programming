#!/usr/bin/python3
'''Displays the value of X-Request-Id'''
import requests


def main(args):
    try:
        r = requests.get(args[1])
        print(r.headers['X-Request-Id'])
    except KeyError:
        pass


if __name__ == '__main__':
    import sys
    main(sys.argv)
