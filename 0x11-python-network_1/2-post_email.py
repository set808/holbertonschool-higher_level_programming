#!/usr/bin/python3
'''Defines a script to send a POST request'''
import urllib.parse
import urllib.request


def main(args):

    url = args[1]
    values = {'email': args[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read()

    print(body.decode('utf8'))


if __name__ == '__main__':
    import sys
    main(sys.argv)
