#!/usr/bin/python3
'''Scirpt for Error Codes'''
import requests

def main(args):
        r.requests.get(args[1])
        if r.status_code >= 400:
            print('Error code: {}'.format(r.status_code))
        else:
            print(r.text)

if __name__ == '__main__':
    import sys
    main(sys.argv)
