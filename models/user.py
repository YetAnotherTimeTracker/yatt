"""
Created by anthony on 19.10.17
user
"""
from sqlalchemy import BigInteger, Column, String, DateTime
import datetime
from config.db_config import Base


class User(Base):
    __tablename__ = 'users'
