"""
Created by anthony on 22.10.17
schedule
"""
from sqlalchemy import BigInteger, Column, String, DateTime, SmallInteger, ForeignKey, Boolean
from config.db_config import Base
import datetime


class Schedule(Base):
    __tablename__ = 'schedules'

    id                      = Column(BigInteger, primary_key=True, autoincrement=True)
    start_datetime          = Column(DateTime, default=datetime.datetime.utcnow)
    end_datetime            = Column(DateTime)
    next_remind_datetime    = Column(DateTime)
    is_periodical           = Column(Boolean, default=False)
    is_active               = Column(Boolean, default=True)
