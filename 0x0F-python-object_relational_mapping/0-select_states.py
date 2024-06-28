#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    # Establishing a connection to the MySQL database
    database = MySQLdb.connect(host='localhost', port=3306,
                               user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Creating a cursor object to interact with the database
    cursor = database.cursor()

    # Executing the SQL query to retrieve all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")

    # Fetching all the rows from the result of the query
    results = cursor.fetchall()

    # Iterating through the rows and printing each one
    for state in results:
        print(state)

    # Closing the cursor and database connection
    cursor.close()
    database.close()
