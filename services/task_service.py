"""
Created by anthony on 22.10.17
task_service

if you are not sure which service should implement function
then function should be implemented in subject's service
e.g. get all tasks of certain project -> subject is project -> project_service.get_all_tasks_by_project
"""
from config.db_config import db_session
from models.task import Task
from models.project import Project
from models.user import User
from services import project_service, user_service
from utils.service_utils import save, flush, find_all


def find_tasks_by_title(title):
    all_tasks = find_all(Task)
    res = []
    for t in all_tasks:
        if title in t.title:
            res.append(t)

    return res


def find_nearest_task(user_id, project_id):
    all_tasks = find_all(Task)
    tasks_by_user_id = filter(
        lambda t: t.get_user_id() == user_id and t.get_project_id() == project_id, all_tasks)

    sorted_by_remind_date = sorted(
        tasks_by_user_id, key=lambda t: t.get_next_remind_date())

    return sorted_by_remind_date[0]


def create_task(update):
    # create or get user
    chat_id = update.message.chat.id
    username = update.message.chat.username
    user = user_service.create_or_get_user(chat_id, username)

    # create or get project
    msg_text = update.message.text
    project = project_service.create_or_get_project(msg_text, user.get_id())

    if project and user:
        new_task = Task(description=msg_text, user_id=user.get_id(), project_id=project.get_id())
        saved_task = save(new_task)

        project_service.update_nearest_task_for_project(project.get_id())

        return saved_task

    else:
        raise ValueError('Project/User could not be created')
