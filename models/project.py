"""
Created by anthony on 19.10.17
project
"""
from sqlalchemy import BigInteger, Column, String, ForeignKey, Boolean
from config.db_config import Base


class Project(Base):
    __tablename__ = 'projects'

    id              = Column(BigInteger, primary_key=True, autoincrement=True)
    title           = Column(String)
    is_active       = Column(Boolean, default=True)
    # fk
    # TODO for sake of simplicity nullable was disabled. enable it
    next_task_id    = Column(BigInteger)#, ForeignKey('tasks.id'), nullable=False)
    user_id         = Column(BigInteger)#, ForeignKey('users.id'), nullable=False)

    def get_id(self):
        return self.id
