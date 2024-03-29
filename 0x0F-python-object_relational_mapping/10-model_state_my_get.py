#!/usr/bin/python3
"""Fetch one unit of data using sqlalchemy"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv as keys

if __name__ == '__main__':
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        keys[1], keys[2], keys[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    row = session.query(State).filter_by(
        name=keys[4]).order_by(State.id).first()
    if (row is None):
        print("Not found")
    else:
        print(row.id)
    session.close()
