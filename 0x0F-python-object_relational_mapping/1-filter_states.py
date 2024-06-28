#!/usr/bin/python3
"""
This script lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa. It takes three arguments: MySQL
username, MySQL password, and the database name. The results are
sorted in ascending order by states.id.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Connect to the MySQL database
    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object to interact with the database
    cur = conn.cursor()

    # Execute the SQL query to retrieve states with names starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC;")

    # Fetch all the rows from the result of the query
    rows = cur.fetchall()

    # Iterate through the rows and print each one
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    conn.close()

