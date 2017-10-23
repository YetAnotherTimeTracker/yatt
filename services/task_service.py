"""
Created by anthony on 22.10.17
task_service
"""
from config.db_config import db_session
import datetime
from models.task import Task
from models.project import Project
from models.user import User
from services import project_service, user_service
from utils.message_parser import message_parser


def save(entity):
    db_session.add(entity)
    db_session.commit()
    return entity


def find_all():
    all_tasks = db_session.query(Task)
    return all_tasks


def find_tasks_by_title(title):
    all_tasks = find_all()
    res = []
    for t in all_tasks:
        if title in t.title:
            res.append(t)

    return res


def find_nearest_task(user_id, project_id):
    all_tasks = find_all()
    tasks_by_user_id = filter(
        lambda t: t.get_user_id() == user_id and t.get_project_id() == project_id, all_tasks)

    sorted_by_remind_date = sorted(
        tasks_by_user_id, key=lambda t: t.get_next_remind_date())

    return sorted_by_remind_date[0]


def create_task(message):
    chat = message.chat
    user = user_service.create_user(chat)

    category = message_parser.parse_message_for_category(message)
    project = project_service.create_project(category, user.get_id())

    if project and user:
        new_task = Task(description=message.text, user_id=user.get_id(), project_id=project.get_id(),
                        priority=1, message_text=message.text)
        saved_task = save(new_task)
        project.set_next_task_id(saved_task.get_id())
        save(project)
        return saved_task

    else:
        raise AssertionError('Project/User does not exist')
