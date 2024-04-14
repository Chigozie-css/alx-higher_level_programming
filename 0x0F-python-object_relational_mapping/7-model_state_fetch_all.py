#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Create the engine to connect to the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    
    """Create the tables based on the provided model"""
    Base.metadata.create_all(engine)
    
    """Create a sessionmaker to interact with the database"""
    Session = sessionmaker(bind=engine)
    session = Session()
    
    """Query the State table and print out the data"""
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
