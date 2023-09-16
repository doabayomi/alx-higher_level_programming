#!/usr/bin/python3
"""Lists all cities by states."""
import sys
import MySQLdb

if __name__ == "__main__":
    u_name = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=u_name,
                         password=pwd, database=db_name)
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id;")
    states = c.fetchall()

    for state in states:
        print(state)
