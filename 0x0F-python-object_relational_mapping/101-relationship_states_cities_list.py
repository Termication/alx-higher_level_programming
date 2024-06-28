#!/usr/bin/python3
"""
Lists all State objects and their corresponding City objects from the database.
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # Create an engine to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create all tables defined by Base's subclasses
    Base.metadata.create_all(engine)

    # Create a sessionmaker to bind the engine to session instances
    Session = sessionmaker(bind=engine)

    # Create a session to interact with the database
    session = Session()

    # Query all State objects with their associated City objects, ordered by
    # State.id and City.id
    states_and_cities = session.query(State).outerjoin(
        City).order_by(State.id, City.id).all()

    # Iterate over each State object and print its id and name
    for state in states_and_cities:
        print("{}: {}".format(state.id, state.name))

        # Iterate over each City object associated with the current State and
        # print its id and name
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    # Close the session to free resources
    session.close()
