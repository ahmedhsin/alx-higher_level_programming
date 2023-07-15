#!/usr/bin/python3
"""Model State using sqlalchemy --v1.4 """
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine, String, Column, Integer

Base = declarative_base()


class State(Base):
    """State Class Mapped to states table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state", cascade="delete")