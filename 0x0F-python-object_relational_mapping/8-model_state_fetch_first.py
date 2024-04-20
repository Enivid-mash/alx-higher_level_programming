#!/usr/bin/python3
"""
Retrieve the first state object from the database
Script parameters: username, password, database.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create an engine for the database
    username = argv[1]
    password = argv[2]
    database = argv[3]
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{database}',
            pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first state instance in the database
    first_instance = session.query(State).order_by(State.id).first()
    if first_instance:
        print(f"{first_instance.id}: {first_instance.name}")
    else:
        print("Nothing")

    session.close()
