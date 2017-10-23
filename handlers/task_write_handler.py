"""
Created by anthony on 18.10.17
task_write_handler
"""
from telegram.ext import CommandHandler
from models.task import Task
from models.schedule import Schedule
from models.project import Project
from services import task_service, schedule_service, project_service


COMMAND = 'write'


def task_write():
    return CommandHandler(COMMAND, _handle)


def _handle(bot, update):
    task_service.create_task(update.message)
    update.message.reply_text('I\'ve created task for ya!')
