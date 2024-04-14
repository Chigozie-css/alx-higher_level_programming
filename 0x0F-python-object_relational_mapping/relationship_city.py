#!/usr/bin/python3
"""
Defines the City class representing cities in the database
"""
from relationship_state import Base  
from sqlalchemy import Column, Integer, String, ForeignKey  
from sqlalchemy.ext.declarative import declarative_base  


class City(Base):
    """
    Represents a city with its attributes
    """
    __tablename__ = 'cities'  
    id = Column(Integer, unique=True, nullable=False, primary_key=True)  
    name = Column(String(128), nullable=False)  
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
