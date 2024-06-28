#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
It takes four arguments: MySQL username, MySQL password, database
name, and state name searched. The results are sorted in ascending
order by states.id.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Connect to the MySQL database
    connection = MySQLdb.connect(host='localhost', port=3306,
                                 user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Execute the SQL query to retrieve states where name matches the argument
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(sys.argv[4])
    cursor.execute(query)

    # Fetch all the rows from the result of the query
    results = cursor.fetchall()

    # Iterate through the rows and print each one
    for state in results:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    connection.close()
