"""
Created by anthony on 23.10.17
project_service
"""
from config.db_config import db_session
from models.project import Project
from services import task_service, user_service


def find_all():
    all_projects = db_session.query(Project)
    return all_projects


def find_all_by_user_id(user_id):
    projects = find_all()
    projects_by_user = []
    for p in projects:
        if user_id == p.get_user_id():
            projects_by_user.append(p)
    return projects_by_user


def find_one_by_id(id_value):
    project_by_id = db_session.query(Project).filter_by(id=id_value).first()
    return project_by_id


def create_project(title, user_id):
    projects_of_user = find_all_by_user_id(user_id)
    # check if theres already a project with same title(category)
    for p in projects_of_user:
        if title == p.get_title():
            return p

    # there were no projects with this title -> create new
    new_proj = _flush(Project(title, user_id))
    saved_proj = _save(new_proj)
    return saved_proj


def _flush(_project):
    db_session.add(_project)
    db_session.flush()
    return _project


def _save(_project):
    db_session.add(_project)
    db_session.commit()
    return _project

