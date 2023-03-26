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
    row = session.query(State).order_by(State.id).first()
<<<<<<< HEAD
    print(row)
    if (row == None):
=======
    if (len(row) == 0):
>>>>>>> 659908eb641985119198cc8451f97800b59e09ce
        print("Nothing")
    else:
        print('{}: {}'.format(row.id, row.name))
    session.close()
