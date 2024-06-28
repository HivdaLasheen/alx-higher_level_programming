#!/usr/bin/python3
"""Definition of the State class with a relationship to City"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City

class State(Base):
    """Class State with a relationship to City"""

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
