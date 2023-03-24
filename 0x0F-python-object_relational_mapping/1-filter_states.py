#!/usr/bin/python3
"""Python with MySQLdb --filter states"""
from MySQLdb import connect
import sys


def main():
    """Main function logic"""

    con = connect(port=3306, user=sys.argv[1],
                  passwd=sys.argv[2], db=sys.argv[3])
    cursor = con.cursor()
    sql = "select id, name from states where name like 'N%';"
    cursor.execute(sql)
    for i in range(cursor.rowcount):
        print(cursor.fetchone())


if __name__ == "__main__":
    main()
