#!/usr/bin/python3
"""
This script deletes all State objects with a name
containing the letter `a` from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connects to the database, deletes State objects
    with a name containing the letter 'a', and commits the changes.
    """

    # Create a database URI from command-line arguments
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    # Create an engine to connect to the database
    engine = create_engine(db_uri)

    # Bind the engine to a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for State objects with a name containing 'a' and delete them
    for instance in session.query(State).filter(State.name.contains('a')):
        session.delete(instance)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
