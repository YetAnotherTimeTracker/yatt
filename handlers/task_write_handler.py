"""
Created by anthony on 18.10.17
task_write_handler
"""
from telegram.ext import CommandHandler
from config.db_config import db_session
from models.task import Task


COMMAND = 'write'


def task_write():
    return CommandHandler(COMMAND, _handle)


def _handle(bot, update):
    msg_text = update.message.text

    task = Task(title="Task Title", description=msg_text)
    db_session.add(task)
    db_session.commit()

    update.message.reply_text('I\'ve created task for ya!')
