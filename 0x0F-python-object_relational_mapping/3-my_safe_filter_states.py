#!/usr/bin/python3
"""Python with MySQLdb filter state using user input --fixing sql injection"""
from MySQLdb import connect
import sys


def main():
    """Main function logic"""

    con = connect(port=3306, user=sys.argv[1],
                  passwd=sys.argv[2], db=sys.argv[3])
    cursor = con.cursor()
    sql = "SELECT * FROM states WHERE name = %(name)s ORDER BY id ASC;"
    cursor.execute(sql, {'name': sys.argv[4]})
    data = cursor.fetchall()
    for row in data:
        if (row[1][:] == sys.argv[4]):
            print(row)

    cursor.close()
    con.close()


if __name__ == "__main__":
    main()
