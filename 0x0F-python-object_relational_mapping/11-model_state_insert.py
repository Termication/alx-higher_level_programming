#!/usr/bin/python3
"""
This script adds the State object
`Louisiana` to the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the database, add the State object
    `Louisiana`, and print its id.
    """

    # Create the database connection URI
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create a new State object with the name 'Louisiana'
    lou_state = State(name='Louisiana')

    # Add the new State object to the session
    session.add(lou_state)

    # Commit the session to the database
    session.commit()

    # Print the id of the newly added State object
    print('{0}'.format(lou_state.id))

    # Close the session
    session.close()
