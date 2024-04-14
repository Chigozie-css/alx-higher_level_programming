#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Create the engine to connect to the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    
    """Create a sessionmaker to interact with the database"""
    Session = sessionmaker(bind=engine)
    session = Session()
    
    """Query all State objects and print out their information"""
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
