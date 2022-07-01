#!/usr/bin/env python3
""" Hash password, Register user, Credentials validation, Generate UUIDs,
    Find user by session ID, Destroy session, Generate reset password token,
    Update password """
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from db import DB
from user import User


def _hash_password(password: str) -> str:
    """ takes in a password string arguments and returns a string
        The returned string is a salted hash of the input password,
        hashed with bcrypt.hashpw """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ return a string representation of a new UUID """
    return str(uuid4())
