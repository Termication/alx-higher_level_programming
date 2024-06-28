#!/usr/bin/python3
"""
Script that lists all cities from
the database `hbtn_0e_4_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    get the cities from the database.
    """

    data = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                           passwd=argv[2], data=argv[3])

    with data.cursor() as cur:
        cur.execute("""
            SELECT
                cities.id, cities.name, states.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            ORDER BY
                cities.id ASC
        """)

        rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
