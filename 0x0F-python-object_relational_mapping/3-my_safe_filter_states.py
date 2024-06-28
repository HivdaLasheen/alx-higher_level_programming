#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument,
and is safe from SQL injections.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Connect to the MySQL database
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query using parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cur.execute(query, (sys.argv[4],))

    # Fetch all the rows from the result of the query
    rows = cur.fetchall()

    # Iterate through the rows and print each one
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
