"""
Created by anthony on 23.10.17
project_service
"""
from config.db_config import db_session
from models import project


def save(_project):
    db_session.add(_project)
    db_session.commit()


def find_all():
    all_projects = db_session.query(project.Project)
    return all_projects
