#!/usr/bin/python3
"""Prints the State object with the name passed as an argument from the database."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Create the engine to connect to the database."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    
    """Create the table in the database."""
    Base.metadata.create_all(engine)
    
    """Create a sessionmaker to interact with the database."""
    Session = sessionmaker(bind=engine)
    session = Session()
    
    """Query the State object with id=2 and update its name to 'New Mexico'."""
    new_instance = session.query(State).filter_by(id=2).first()
    new_instance.name = 'New Mexico'
    
    """Commit the changes to the database."""
    session.commit()
