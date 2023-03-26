#!/usr/bin/python3
"""fetch all citys with its respective state"""
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
import sys
from sqlalchemy import create_engine

if __name__ == '__main__':
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    )
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()
    for row in data:
        print('{}: ({}) {}'.format(
            row[1].name,
            row[0].id,
            row[0].name
        ))
