#!/usr/bin/python3
"""Filter states based on matching arguments"""
import sys
import MySQLdb

if __name__ == "__main__":
    u_name = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=u_name,
                         password=pwd, database=db_name)
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name='{}';".format(state))
    states = c.fetchall()

    for state in states:
        print(state)
