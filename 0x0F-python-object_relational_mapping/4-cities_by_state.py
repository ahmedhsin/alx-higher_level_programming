#!/usr/bin/python3
"""Python with MySQLdb show citites and states"""
from MySQLdb import connect
import sys


def main():
    """Main function logic"""

    con = connect(port=3306, user=sys.argv[1],
                  passwd=sys.argv[2], db=sys.argv[3])
    cursor = con.cursor()
    sql = "SELECT cities.id, cities.name, states.name\
        FROM cities JOIN states ON cities.state_id = states.id\
        ORDER BY cities.id;"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row)

    cursor.close()
    con.close()


if __name__ == "__main__":
    main()
