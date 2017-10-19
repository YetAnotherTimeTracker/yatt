"""
Created by anthony on 18.10.17
task_read_handler
"""
from telegram.ext import CommandHandler
from config.db_config import db_session
from models.task import Task


COMMAND = 'read'


def task_read():
    return CommandHandler(COMMAND, _handle)


def _handle(bot, update):

    current_tasks = []

    all_tasks = db_session.query(Task)
    for task in all_tasks:
        current_tasks.append(task.description)

    update.message.reply_text(f'Here are your tasks:\n{current_tasks}')
