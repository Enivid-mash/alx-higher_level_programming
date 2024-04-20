#!/usr/bin/python3
"""
Retrieve all state objects from the database using Python.
Script parameters: username, password, database.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

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

    # Query state instances in the database
    for instance in session.query(State).order_by(State.id):
        print(f"{instance.id}: {instance.name}")

    session.close()
