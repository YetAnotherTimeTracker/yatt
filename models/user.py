"""
Created by anthony on 19.10.17
user
"""
from sqlalchemy import BigInteger, Column, String, Boolean
from config.db_config import Base


class User(Base):
    __tablename__ = 'users'
    id              = Column(BigInteger, primary_key=True, autoincrement=True)
    username        = Column(String)
    chat_id         = Column(String)
    # safe delete flag
    is_active       = Column(Boolean, default=True)

    def __init__(self, username, chat_id):
        self.set_username(username)
        self.set_chat_id(chat_id)

    def get_id(self):
        return self.id

    def get_username(self):
        return self.username

    def set_username(self, name):
        self.username = name

    def get_chat_id(self):
        return self.chat_id

    def set_chat_id(self, chat_id):
        if not chat_id:
            raise ValueError('User\'s chat id cannot be empty')
        self.chat_id = chat_id
