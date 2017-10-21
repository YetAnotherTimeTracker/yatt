"""
Created by anthony on 19.10.17
project
"""
from sqlalchemy import BigInteger, Column, String, DateTime
import datetime
from config.db_config import Base


class Project(Base):
    __tablename__ = 'projects'

