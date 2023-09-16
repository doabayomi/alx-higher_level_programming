#!/usr/bin/python3
"""Lists all states."""
import sys
import MySQLdb

u_name = sys.argv[1]
pwd = sys.argv[2]
db_name = sys.argv[3]
db = MySQLdb._mysql.connect(host="localhost", port=3306, user=u_name,  password=pwd, database=db_name)
db.query("""SELECT * FROM states""")
r = db.store_result()
for i in r.fetch_row(maxrows=0):
    print(i);
