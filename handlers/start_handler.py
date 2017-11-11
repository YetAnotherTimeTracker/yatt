"""
Created by anthony on 15.10.17
start_handler
"""
from telegram.ext import CommandHandler
from services import user_service


COMMAND_START = 'start'


def start():
    return CommandHandler(COMMAND_START, _handle_start)


def _handle_start(bot, update):
    reply_msg = 'Hello'

    try:
        chat = update.message.chat
        user = user_service.create_or_get_user(chat)

        if user:
            reply_msg += ', ' + user.get_first_name()

        update.message.reply_text(reply_msg)

    except Exception as e:
        update.message.reply_text(reply_msg)
