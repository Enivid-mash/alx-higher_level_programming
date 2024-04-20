#!/usr/bin/python3
"""
Return matching states with parameters provided to the script: username,
password, database, and state to match.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute("""SELECT * FROM states WHERE
            name LIKE '{:s}' ORDER BY id ASC""".format(argv[4]))

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        if row[1] == argv[4]:
            print(row)
    db_cursor.close()
    db_connect.close()
