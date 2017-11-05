"""
Created by anthony on 23.10.17
project_service
"""
from config.db_config import db_session
from models.project import Project
from models.task import Task
from services import task_service, user_service
from utils.message_parser import message_parser
from utils.service_utils import save, flush, find_all, find_one_by_id


def find_all_by_user_id(user_id):
    projects = find_all(Project)
    projects_by_user = [user_id == p.get_user_id() for p in projects]
    return projects_by_user


def create_or_get_project(message, user_id):
    # TODO somehow find out message's category
    title = message_parser.parse_message_for_project(message)

    projects_of_user = find_all_by_user_id(user_id)
    # check if theres already a project with same title(category)
    for p in projects_of_user:
        if title == p.get_title():
            return p

    # there is no project with this title -> create new
    new_proj = flush(Project(title, user_id))
    saved_proj = save(new_proj)
    return saved_proj


def update_nearest_task_for_project(project_id_value):
    # try cast to int to prevent getting project here. we need only it's id here
    project_id = int(project_id_value)
    project = find_one_by_id(project_id, Project)

    if project:
        all_tasks = find_all(Task)
        tasks_by_project_id = [a.get_project_id() == project_id for a in all_tasks]
        sorted_by_next_remind_date = filter(lambda t: t.get_next_remind_date(), tasks_by_project_id)

        nearest_task = next(sorted_by_next_remind_date)
        if nearest_task:
            project.set_next_task_id(next(sorted_by_next_remind_date))
            saved_proj = save(project)
            return saved_proj
