#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" from a DB
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """Create the engine to connect to the database."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    
    """Create the tables in the database."""
    Base.metadata.create_all(engine)

    """Create a sessionmaker to interact with the database."""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Create a new State object 'California' and a new City object 'San Francisco'."""
    newState = State(name='California')
    newCity = City(name='San Francisco')
    
    """Associate the new City object with the new State object."""
    newState.cities.append(newCity)

    """Add the new State and City objects to the session and commit the changes."""
    session.add(newState)
    session.add(newCity)
    session.commit()
