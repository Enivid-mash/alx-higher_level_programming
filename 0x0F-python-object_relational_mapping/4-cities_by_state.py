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

    query = """SELECT cities.id, cities.name, states.name FROM states INNER
    JOIN cities ON states.id = cities.state_id ORDER BY cities.id ASC"""

    db_cursor.execute(query)

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)

    db_cursor.close()
    db_connect.close()
