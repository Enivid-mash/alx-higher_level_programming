#!/usr/bin/python3
"""
Retrieve state objects containing the letter 'a' from the database
Script parameters: username, password, database
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

    # Query state instances in the database containing the letter 'a'
    for state in session.query(
            State).filter(State.name.like('%a%')).order_by(State.id):
        print(f"{state.id}: {state.name}")

    session.close()
