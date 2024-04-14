#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects from the database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Create the engine to connect to the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    """Create the tables in the database"""
    Base.metadata.create_all(engine)

    """Create a sessionmaker to interact with the database"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Query all State objects with their associated City objects, sorted by state and city IDs"""
    states = session.query(State).order_by(State.id).all()

    """Loop through each State object and print its name along with its associated City objects"""
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
