"""
Created by anthony on 15.10.17
echo_handler
"""
from telegram.ext import MessageHandler, Filters
from services import task_service, user_service


def echo():
    return MessageHandler(Filters.text, _handle)


def _handle(bot, update):
    try:
        new_task = task_service.create_task(update)

        if new_task:
            reply_on_success = f'task with id "{new_task.get_id()}" has been created!'

            chat_id = update.message.chat.id
            user = user_service.find_one_by_id(chat_id)
            if user:
                reply_on_success = user.get_first_name() + ', ' + reply_on_success

            update.message.reply_text(reply_on_success.capitalize())

    except Exception as e:
        reply_on_error = f'Sorry, there were an error: {e}'
        update.message.reply_text(reply_on_error)
        return
