"""
Created by anthony on 23.10.17
user_service.py
"""
from config.db_config import db_session
import datetime
from models.task import Task
from models.project import Project
from models.user import User


def find_all():
    users = db_session.query(User)
    return users


def find_one_by_id(id_value):
    users = find_all()
    for u in users:
        if id_value == u.get_id():
            return u
    return None


def find_one_by_username(username):
    users = find_all()
    for u in users:
        if username == u.get_username():
            return u
    return None


def create_user(chat):
    username = chat.username
    # check if user already exists
    user_by_name = find_one_by_username(username)
    if user_by_name:
        return user_by_name

    else:
        # create new one
        user = _flush(User(username, chat.id))
        saved_user = _save(user)
        return saved_user


def _flush(_user):
    """ prepare user (fill _id_ attribute but do _not_ insert) """
    db_session.add(_user)
    db_session.flush()
    return _user


def _save(_user):
    """ insert user into db """
    db_session.add(_user)
    db_session.commit()
    return _user
