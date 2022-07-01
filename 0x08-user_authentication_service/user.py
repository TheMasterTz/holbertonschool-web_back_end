#!/usr/bin/env python3
"""User model"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, null
Base = declarative_base()


class User(Base):
    """
    User _summary_

    Args:
        Base (_type_): _description_
    """
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(Integer, nullable=True)
    reset_token = Column(String(250), nullable=True)
