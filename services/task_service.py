"""
Created by anthony on 22.10.17
task_service

if you are not sure which service should implement function
then implement it in it's return type service
e.g. get all user's tasks: return type is Task -> task_service.find_all_by_user_id
"""
from models.task import Task
from services import project_service, user_service
from utils.service_utils import save, find_all, find_one_by_id


def find_tasks_by_title(title):
    all_tasks = find_all(Task)
    res = []
    for t in all_tasks:
        if title in t.title:
            res.append(t)

    return res


def find_task_by_id_and_user_id(task_id_value, user_id):
    task_id = int(task_id_value)
    task_by_id = find_one_by_id(task_id, Task)

    if task_by_id and task_by_id.get_user_id() == user_id:
        return task_by_id

    else:
        return None


def find_tasks_by_user_id(user_id_value):
    user_id = int(user_id_value)
    all_tasks = find_all(Task)
    tasks_by_user = [t for t in all_tasks if user_id == t.get_user_id()]
    return tasks_by_user


def find_nearest_task(user_id, project_id):
    all_tasks = find_all(Task)
    tasks_by_user_id = filter(
        lambda t: t.get_user_id() == user_id and t.get_project_id() == project_id, all_tasks)

    sorted_by_remind_date = sorted(
        tasks_by_user_id, key=lambda t: t.get_next_remind_date())

    return sorted_by_remind_date[0]


def create_task(update):
    # create or get user
    chat = update.message.chat
    user = user_service.create_or_get_user(chat)

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
