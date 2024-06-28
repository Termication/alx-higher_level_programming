#!/usr/bin/python3
"""
This script prints all City objects
from the database `hbtn_0e_14_usa`.
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connects to the database, retrieves all City objects,
    and prints each city's name along with its state's name.
    """

    # Create a database URI from command-line arguments
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    # Create an engine to connect to the database
    engine = create_engine(db_uri)

    # Bind the engine to a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to retrieve all City objects and their corresponding State
    query = session.query(City, State).join(State)

    # Print each city with its state's name
    for city, state in query.all():
        print("{}: ({:d}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()
