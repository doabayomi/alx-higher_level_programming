#!/usr/bin/python3
"""Switches out the name of a state with id 2"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    u_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(u_name, password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_to_update = session.query(State).filter(State.id == 2).first()

    if state_to_update:
        state_to_update.name = 'New Mexico'
        session.commit()
