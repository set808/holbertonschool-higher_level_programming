#!/usr/bin/python3
'''Defines script to display the body of response'''
import urllib.request


def main(args):

    url = args[1]
    req = urllib.request.Request(url)
    try:
        urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print('Error code: {}'.format(e.code))

if __name__ == '__main__':
    import sys
    main(sys.argv)
