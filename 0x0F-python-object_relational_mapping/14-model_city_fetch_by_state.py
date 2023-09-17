#!/usr/bin/python3
"""Prints all city objects in the database"""
import sys
from model_state import Base, State
from model_city import City
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

    state_cities = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in state_cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
