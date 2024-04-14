#!/usr/bin/python3
"""
Contains the class definition of a State with a relationship to City
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    Class that defines each state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    cities = relationship("City", backref="state")
