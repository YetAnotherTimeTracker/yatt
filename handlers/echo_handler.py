"""
Created by anthony on 15.10.17
echo_handler
"""
from telegram.ext import MessageHandler, Filters


def echo():
    return MessageHandler(Filters.text, _handle_echo)


def _handle_echo(bot, update):
    update.message.reply_text(f'You said "{update.message.text}"')
