#!/usr/bin/python3
"""Definition of the City class
"""

# from sqlalchemy.ext.declarative import declarative_base (for sqlalchemy 1.3)
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from relationship_state import Base


class City(Base):
    """Class City"""

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
