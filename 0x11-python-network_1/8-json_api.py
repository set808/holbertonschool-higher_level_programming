#!/usr/bin/python3
'''Sends a POST request'''
import requests


def main(args):
    if len(args) == 1:
        data = ''
    else:
        data = args[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': data})
    try:
        json = r.json()
        if json:
            print('[{}] {}'.format(json['id'], json['name']))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')

if __name__ == '__main__':
    import sys
    main(sys.argv)
