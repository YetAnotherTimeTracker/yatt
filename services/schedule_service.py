"""
Created by anthony on 23.10.17
schedule_service
"""
from config.db_config import db_session
from models import schedule


def save(_schedule):
    db_session.add(_schedule)
    db_session.commit()


def find_all():
    all_schedules = db_session.query(schedule.Schedule)
    return all_schedules
