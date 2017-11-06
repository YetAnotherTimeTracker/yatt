"""
Created by anthony on 18.10.17
task_read_handler
"""
from telegram.ext import CommandHandler
from models.task import Task
from services import task_service, user_service

COMMAND = 'read'


def task_read():
    return CommandHandler(COMMAND, _handle)


def _handle(bot, update):
    chat_id = update.message.chat.id
    user = user_service.find_one_by_chat_id(chat_id)
    user_tasks = task_service.find_tasks_by_user_id(user.get_id())

    tasks_to_show = [t.get_description() for t in user_tasks]

    first_name = user.get_first_name()
    if 0 == len(tasks_to_show):
        update.message.reply_text(f'{first_name}, you don\'t have any tasks yet')
        update.message.reply_text('Just write me something to create new one :)')

    else:
        update.message.reply_text(f'{first_name}, here are your tasks:\n{tasks_to_show}')
