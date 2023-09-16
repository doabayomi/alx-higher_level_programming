#!/usr/bin/python3
"""Filter states based on matching arguments safely"""
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
    c.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id \
    WHERE states.name=%s;", (state,))
    states = c.fetchall()

    final_output = ""
    for state in states:
        final_output += state[1] + ", "

    print(final_output[:-2:])
