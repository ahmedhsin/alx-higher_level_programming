#!/usr/bin/python3
"""Python with MySQLdb show citites and states filter states"""
from MySQLdb import connect
import sys


def main():
    """Main function logic"""

    con = connect(port=3306, user=sys.argv[1],
                  passwd=sys.argv[2], db=sys.argv[3])
    cursor = con.cursor()
    sql = "SELECT cities.id, cities.name, states.name\
        FROM cities JOIN states ON cities.state_id = states.id\
        WHERE states.name = %(name)s\
        ORDER BY cities.id;"
    cursor.execute(sql, {'name': sys.argv[4]})
    data = cursor.fetchall()
    query = []
    for row in data:
        if (row[2] == sys.argv[4]):
            query.append(row[1])
    print(', '.join(query))
    cursor.close()
    con.close()


if __name__ == "__main__":
    main()
