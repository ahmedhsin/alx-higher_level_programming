#!/usr/bin/python3
"""Fetch all  using sqlalchemy"""
from relationship_state import Base, State
from relationship_city import City
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
    cities = session.query(City).all()
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
