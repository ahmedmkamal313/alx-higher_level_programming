#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states
where `name` matches the argument from the database `hbtn_0e_0_usa`.
This time the script is safe from
MySQL injections!
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]
