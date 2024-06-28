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
    connection = MySQLdb.connect(host='localhost', port=3306,
                                 user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Execute the SQL query to retrieve states with names starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC;")

    # Fetch all the rows from the result of the query
    results = cursor.fetchall()

    # Iterate through the rows and print each one
    for state in results:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    connection.close()
