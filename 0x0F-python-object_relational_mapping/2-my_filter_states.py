#!/usr/bin/python3
"""Python with MySQLdb filter state using user input"""
from MySQLdb import connect
import sys


def main():
    """Main function logic"""

    con = connect(port=3306, user=sys.argv[1],
                  passwd=sys.argv[2], db=sys.argv[3])
    cursor = con.cursor()
    sql = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;".format(
        sys.argv[4])
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row)

    cursor.close()
    con.close()


if __name__ == "__main__":
    main()
