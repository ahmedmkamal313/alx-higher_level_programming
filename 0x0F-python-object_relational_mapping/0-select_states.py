#!/usr/bin/python3
# Import MySQLdb module
import MySQLdb
# Import sys module to get command line arguments
import sys

# Get the arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

# Connect to the MySQL server
db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
        )

# Create a cursor object
cursor = db.cursor()

# Execute the SQL query to select all states
cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

# Fetch all the rows from the cursor
rows = cursor.fetchall()

# Loop through the rows and print each state
for row in rows:
    print(row)

# Close the cursor and the database connection
cursor.close()
db.close()
