"""
Created by anthony on 23.10.17
user_service.py
"""
from config.db_config import db_session
import datetime
from models.task import Task
from models.project import Project
from models.user import User
from utils.service_utils import save, flush, find_all, find_one_by_id


def find_one_by_username(username):
    users = find_all(User)
    for u in users:
        if username == u.get_username():
            return u
    return None


def create_or_get_user(chat):
    chat_id = int(chat.id)
    # check if user already exists
    user_by_id = find_one_by_id(chat_id, User)
    if user_by_id:
        return user_by_id

    else:
        # create new one
        username = chat.username
        first_name = chat.first_name
        user = flush(User(username=username, chat_id=chat_id, first_name=first_name))
        saved_user = save(user)
        return saved_user
