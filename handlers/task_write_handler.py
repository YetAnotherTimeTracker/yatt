"""
Created by anthony on 18.10.17
task_write_handler
"""
from telegram.ext import CommandHandler
from services import task_service, project_service


COMMAND = 'write'


def task_write():
    return CommandHandler(COMMAND, _handle)


def _handle(bot, update):
    reply_text = 'I\'ve created task for ya!'
    try:
        task_service.create_task(update.message)

    except Exception as e:
        reply_text = 'There was an error' + e

    update.message.reply_text(reply_text)
