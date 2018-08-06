#!/usr/bin/python3
'''Scirpt for Error Codes'''
import requests

def main(args):
    r = requests.get(args[1])
    try:
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError:
        print('Error code: {}'.format(r.status_code))

if __name__ == '__main__':
    import sys
    main(sys.argv)
