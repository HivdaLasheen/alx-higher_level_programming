#!/usr/bin/python3
"""
takes in the name of a state as an argument and
lists all cities of that state,
using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Connect to the MySQL database
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query to retrieve cities of the specified state
    cur.execute("SELECT cities.name \
                FROM cities \
                LEFT JOIN states ON states.id = cities.state_id \
                WHERE states.name = %s \
                ORDER BY cities.id ASC", (sys.argv[4],))

    # Fetch all the rows from the result of the query
    rows = cur.fetchall()

    # Print the cities in the required format
    print(", ".join([row[0] for row in rows]))

    # Close the cursor and database connection
    cur.close()
    db.close()
