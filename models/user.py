"""
Created by anthony on 19.10.17
user
"""
from sqlalchemy import BigInteger, Column, String
from config.db_config import Base


class User(Base):
    __tablename__ = 'users'

    id              = Column(BigInteger, primary_key=True, autoincrement=True)
    username        = Column(String, nullable=False)
