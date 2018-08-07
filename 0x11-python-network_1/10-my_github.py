#!/usr/bin/python3
'''Gets Github ID'''
import requests


def main(args):

    username = args[1]
    password = args[2]
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(username, password))
    try:
        print(r.json().get('id'))
    except:
        pass

if __name__ == '__main__':
    import sys
    main(sys.argv)

