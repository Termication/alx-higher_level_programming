#!/usr/bin/python3
"""
This script defines a City class to work with SQLAlchemy ORM.
"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    City class for representing a city in the database.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Cities.
        id (int): The city's unique identifier.
        name (str): The city's name.
        state_id (int): The id of the state to which the city belongs.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
