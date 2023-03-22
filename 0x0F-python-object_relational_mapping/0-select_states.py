#!/usr/bin/python3
"""Python with MySQLdb"""
from MySQLdb import connect
import sys


username = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]


def main():
    """Main function logic"""
    con = connect(port=3306, user=username, passwd=password, db=db_name)
    cursor = con.cursor()
    sql = "select id, name from states order by id;"
    cursor.execute(sql)
    for i in range(cursor.rowcount):
        print(cursor.fetchone())


if __name__ == "__main__":
    main()

