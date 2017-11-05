"""
Created by anthony on 05.11.17
service_utils
"""
from config.db_config import db_session


def save(entity):
    """ insert entity into db """
    db_session.add(entity)
    db_session.commit()
    return entity


def flush(entity):
    """ prepare entity for insertion (fill _id_ attribute but do _not_ insert) """
    db_session.add(entity)
    db_session.flush()
    return entity
