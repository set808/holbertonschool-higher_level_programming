#!/usr/bin/python3
'''Function that filters by user input'''
import MySQLdb


def main(argv):

    if len(argv) != 5:
        print('Incorrect number of arguments')
        return

    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name \
    LIKE "{:s}" ORDER BY id ASC'.format(argv[4]))

    for row in cur.fetchall():
        print(row)

    db.close()

if __name__ == '__main__':
    from sys import argv
    main(argv)
