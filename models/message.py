"""
Created by anthony on 22.10.17
message
"""
from sqlalchemy import BigInteger, Column, String, DateTime, ForeignKey, Boolean
from config.db_config import Base
import datetime


class Message(Base):
    __tablename__ = 'messages'

    id              = Column(BigInteger, primary_key=True, autoincrement=True)
    chat_id         = Column(BigInteger, nullable=False)
    text            = Column(String)
    receive_time    = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    is_active       = Column(Boolean, default=True)
    # fk
    sender_id       = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    receiver_id     = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    task_id         = Column(BigInteger, ForeignKey('tasks.id'), nullable=False)
