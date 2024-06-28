#!/usr/bin/python3
"""
This script prints the id of the State object
with the name passed as an argument
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the database and retrieve the state
    with the specified name.
    """

    # Create the database connection URI
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the State object with the specified name
    instance = session.query(State).filter(State.name == argv[4]).first()

    # Print the state id if found, otherwise print 'Not found'
    if instance is None:
        print('Not found')
    else:
        print('{0}'.format(instance.id))
