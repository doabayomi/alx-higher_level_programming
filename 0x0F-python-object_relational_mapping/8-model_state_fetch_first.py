#!/usr/bin/python3
"""Prints first state object."""
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

    state = session.query(State).order_by(State.id).first()

    print("Nothing" if not state else "{}: {}".format(state.id, state.name))
