#!/usr/bin/python3
'''Function that filters states'''
import MySQLdb


def main(argv):

    if len(argv) != 4:
        print('Incorrect number of arguments')
        return

    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE "N%" ORDER BY id ASC')

    for row in cur.fetchall():
        print(row)

    db.close()

if __name__ == '__main__':
    from sys import argv
    main(argv)
