#!/usr/bin/python3
"""
This script prints all City objects from the database `hbtn_0e_14_usa`.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the database, add a State and a City object, and commit the changes.
    """

    # Create the database URI using command-line arguments for MySQL
    # credentials and database name
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    # Create an engine that stores data in the local MySQL server
    engine = create_engine(db_uri)

    # Create all tables in the database which are defined by Base's subclasses
    Base.metadata.create_all(engine)

    # Bind the engine to the session and create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance to interact with the database
    session = Session()

    # Create a new State object
    cal_state = State(name='California')

    # Create a new City object
    sfr_city = City(name='San Francisco')

    # Append the City object to the State object's cities relationship
    cal_state.cities.append(sfr_city)

    # Add the State object (and the related City object) to the session
    session.add(cal_state)

    # Commit the transaction to the database
    session.commit()

    # Close the session to free resources
    session.close()
