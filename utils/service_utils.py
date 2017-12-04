"""
Created by anthony on 05.11.17
service_utils

only generics should be here
"""
from config.db_config import db_session
import logging


log = logging.getLogger(__name__)


def find_all(entity_class):
    try:
        all_entries = db_session.query(entity_class)
        # db_session.commit()
        return all_entries

    except:
        log.critical(f'Rolling back and closing "find_all" session for entity {entity_class}!')
        db_session.rollback()
        return []

    # finally:
    #     db_session.close()


def find_one_by_id(id_value, entity_class):
    """ assuming id is unique, get entity of entity_class by it """
    id_int = None
    try:
        id_int = int(id_value)

    except ValueError as e:
        err_cause = 'Provided value is not valid id'
        raise ValueError(err_cause)

    try:
        entity_by_id = db_session.query(entity_class) \
            .filter_by(id=id_int) \
            .first()
        # here can be none if nothing found!
        # db_session.commit()
        return entity_by_id

    except:
        log.critical(f'Rolling back and closing "find_one_by_id" session '
                     f'for id ({id_int}) of {entity_class} class!')
        db_session.rollback()
        return None

    # finally:
    #     db_session.close()


def save(entity):
    """ insert entity into db """
    try:
        db_session.add(entity)
        db_session.commit()
        return entity

    except:
        log.critical(f'Rolling back and closing "save" session for entity {entity}!')
        db_session.rollback()
        return entity

    # finally:
        # db_session.close()


def flush(entity):
    """ prepare entity for insertion (fill id attribute but do _not_ insert) """
    try:
        db_session.add(entity)
        db_session.flush()
        return entity

    except:
        log.critical(f'Rolling back and closing "flush" session for entity {entity}!')
        db_session.rollback()
        return entity

    # finally:
    #     db_session.close()
