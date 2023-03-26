#!/usr/bin/python3
"""Model city using sqlalchemy --v1.4 """
from sqlalchemy.orm import declarative_base
from model_state import Base
from sqlalchemy import create_engine, String, Column, Integer, ForeignKey


class City(Base):
    """city Class Mapped to states table"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
