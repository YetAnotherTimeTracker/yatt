"""
Created by anthony on 15.10.17
echo_handler
"""
from telegram.ext import MessageHandler, Filters
from services import task_service, user_service
from bot import w


def echo():
    return MessageHandler(Filters.text, _handle)


def _handle(bot, update):
    chat_id = update.message.chat.id
    user = user_service.find_one_by_chat_id(chat_id)
    first_name = user.get_first_name()

    new_task = None
    try:
        print(w.queue)
        new_task = task_service.create_task(update)

    except Exception as e:
        reply_on_error = f'Sorry, there were an error: {e}'
        update.message.reply_text(reply_on_error)

    if new_task:
        reply_on_success = f'{first_name}, task with id "{new_task.get_id()}" has been created!'
        update.message.reply_text(reply_on_success)
