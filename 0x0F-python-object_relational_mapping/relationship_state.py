#!/usr/bin/python3
"""Definition of the State class with relationship City
"""

# from sqlalchemy.ext.declarative import declarative_base (for sqlalchemy 1.3)
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String
# base class for our classes definitions.
Base = declarative_base()


class State(Base):
    """Class State
    creates and maps the State class
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete-orphan',
                          backref="state")
