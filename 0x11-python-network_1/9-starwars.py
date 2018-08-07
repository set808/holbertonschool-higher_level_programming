#!/usr/bin/python3
'''Sends a search request to Star Wars API'''
import requests


def main(args):
    r = requests.get("https://swapi.co/api/people/?search=" + args[1])
    r = r.json()
    print('Number of results: {}'.format(r['count']))
    if r['count'] != 0:
        for result in r['results']:
            print(result['name'])


if __name__ == '__main__':
    import sys
    main(sys.argv)
