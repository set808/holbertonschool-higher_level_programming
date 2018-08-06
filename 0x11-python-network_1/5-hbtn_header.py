#!/usr/bin/python3
'''Displays the value of X-Request-Id'''
import requests


def main(args):
    r = requests.get(args[1])
    print(r.headers['X-Request-Id'])

if __name__ == '__main__':
    import sys
    main(sys.argv)
