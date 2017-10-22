"""
Created by anthony on 22.10.17
task_service
"""
from config.db_config import db_session
from models.task import Task
from models.schedule import Schedule
from models.project import Project
from services import schedule_service, project_service


def save(_task):
    db_session.add(_task)
    db_session.commit()


def find_all():
    all_tasks = db_session.query(Task)
    return all_tasks


# TODO move search query into db
def find_tasks_by_title(title):
    all_tasks = find_all()
    res = []
    for t in all_tasks:
        if title in t.title:
            res.append(t)

    return res


def create_task(message):
    schedule = Schedule()
    schedule_service.save(schedule)

    project = Project(next_task_id=None, user_id=None)
    project_service.save(project)

    task = Task(title='Task', description=message.text,
                message_id=None, schedule_id=schedule.get_id(), project_id=project.get_id())
    save(task)
