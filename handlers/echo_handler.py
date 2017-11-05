"""
Created by anthony on 15.10.17
echo_handler
"""
from telegram.ext import MessageHandler, Filters
from services import task_service


def echo():
    return MessageHandler(Filters.text, _handle)


def _handle(bot, update):
    new_task = None
    try:
        new_task = task_service.create_task(update)

    except Exception as e:
        reply_on_error = f'Sorry, error has occured: {e}'
        update.message.reply_text(reply_on_error)

    if new_task:
        reply_on_success = f'Task with id "{new_task.get_id()}" has been created!'
        update.message.reply_text(reply_on_success)
