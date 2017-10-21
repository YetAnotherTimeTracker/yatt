"""
Created by anthony on 18.10.17
task
"""
from sqlalchemy import BigInteger, Column, String, DateTime, SmallInteger, ForeignKey, Boolean
from config.db_config import Base
import datetime


class Task(Base):
    __tablename__ = 'tasks'

    id              = Column(BigInteger, primary_key=True, autoincrement=True)
    title           = Column(String)
    description     = Column(String, nullable=False)
    create_date     = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    priority        = Column(SmallInteger, default=1)
    is_active       = Column(Boolean, default=True)
    # fk
    message_id      = Column(BigInteger, ForeignKey('messages.id'), nullable=True)
    schedule_id     = Column(BigInteger, ForeignKey('schedules.id'), nullable=False)
    project_id      = Column(BigInteger, ForeignKey('projects.id'), nullable=False)
