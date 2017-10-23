"""
Created by anthony on 18.10.17
task_read_handler
"""
from telegram.ext import CommandHandler
from models.task import Task
from services import task_service


COMMAND = 'read'


def task_read():
    return CommandHandler(COMMAND, _handle)


def _handle(bot, update):

    current_tasks = []

    all_tasks = task_service.find_all()
    for task in all_tasks:
        current_tasks.append(task.get_description())

    update.message.reply_text(f'Here are your tasks:\n{current_tasks}')
