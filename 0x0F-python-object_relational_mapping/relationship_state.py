#!/usr/bin/python3
"""
Contains the class definition of a State with relationship to City
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base

class State(Base):
    """
    Class with id and name attributes of each state and relationship to City
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
