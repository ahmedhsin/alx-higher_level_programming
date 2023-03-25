#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from MySQLdb import connect

if __name__ == '__main__':
    Base = declarative_base()

    engine = create_engine(
        "mysql+pymysql://test:123456789@localhost/mydb", echo=True)

    class User(Base):
        __tablename__ = 'Users'
        id = Column(Integer, primary_key=True)
        name = Column(String(20))
        fullname = Column(String(20))
        nick_name = Column(String(20))
    Base.metadata.create_all(engine)
