#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Create the engine to connect to the database."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    
    """Create a sessionmaker to interact with the database."""
    Session = sessionmaker(bind=engine)
    session = Session()
    
    """Query the first State object from the database."""
    instance = session.query(State).first()
    if instance is None:
        print("Nothing")
    else:
        print(instance.id, instance.name, sep=": ")
