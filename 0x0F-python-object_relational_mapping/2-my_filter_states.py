#!/usr/bin/python3
"""Python with MySQLdb filter state using user input"""
from MySQLdb import connect
import sys


def main():
    """Main function logic"""

    con = connect(port=3306, user=sys.argv[1],
                  passwd=sys.argv[2], db=sys.argv[3])
    cursor = con.cursor()
    sql = "select * from states where name = '{}' order by id asc;".format(
        sys.argv[4])
    cursor.execute(sql)
    data = cursor.fetchall()
    for i in data:
        print(i)

    cursor.close()
    con.close()


if __name__ == "__main__":
    main()
