#!/usr/bin/python3
"""changes the name of a State object from the database hbtn_0e_6_usa"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

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

    # Query the State object with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Update the state's name if it exists
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
