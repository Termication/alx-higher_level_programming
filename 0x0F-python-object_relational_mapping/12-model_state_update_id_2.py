#!/usr/bin/python3
"""
Script that changes the name of a State object
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Update the name of a State object in the database.
    """

    # Create the database connection URI
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a Session
    session = Session()

    # Query for the State object with id 2
    ari_state = session.query(State).filter(State.id == '2').first()
    
    # Change the name of the State object
    ari_state.name = 'New Mexico'
    
    # Commit the session to save the change
    session.commit()
    
    # Close the session
    session.close()
