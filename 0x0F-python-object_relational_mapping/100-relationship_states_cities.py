#!/usr/bin/python3
"""creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa"""

if __name__ == "__main__":

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from relationship_state import Base, State
    from relationship_city import City

    # Connect to the MySQL server using command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create a session
    session = Session(engine)

    # Create a new State and City
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)

    # Add the new State (and City) to the session
    session.add(new_state)
    session.commit()

    # Close the session
    session.close()
