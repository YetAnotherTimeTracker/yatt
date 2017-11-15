"""
Created by anthony on 05.11.17
service_utils

only generics should be here
"""
from config.db_config import db_session


def find_all(entity_class):
    all_entities = db_session.query(entity_class)
    return all_entities


def find_one_by_id(id_value, entity_class):
    """ assuming id is unique, get entity of entity_class by it """
    id_int = None
    try:
        id_int = int(id_value)

    except ValueError as e:
        err_cause = 'Provided value is not valid id'
        raise ValueError(err_cause)

    entity_by_id = db_session.query(entity_class) \
        .filter_by(id=id_int) \
        .first()
    # here can be none if nothing found!
    return entity_by_id


def save(entity):
    """ insert entity into db """
    db_session.add(entity)
    db_session.commit()
    return entity


def flush(entity):
    """ prepare entity for insertion (fill id attribute but do _not_ insert) """
    db_session.add(entity)
    db_session.flush()
    return entity
