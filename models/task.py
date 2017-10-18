"""
Created by anthony on 18.10.17
task
"""
from sqlalchemy import BigInteger, Column, String, DateTime
import datetime
from config.db_config import Base


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String)
    create_date = Column(DateTime, default=datetime.datetime.utcnow)
