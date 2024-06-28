#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa
sorted by cities.id.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Connect to the MySQL database
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query to retrieve all cities with their corresponding state names
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities LEFT JOIN states \
                ON states.id = cities.state_id \
                ORDER BY cities.id ASC")

    # Fetch all the rows from the result of the query
    rows = cur.fetchall()

    # Iterate through the rows and print each city with its state
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
