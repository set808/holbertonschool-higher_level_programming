#!/usr/bin/python3
'''Defines a script for POST request'''
import requests


def main(args):

    r = requests.post(args[1], data={'email': args[2]})
    print(r.text)


if __name__ == '__main__':
    import sys
    main(sys.argv)
