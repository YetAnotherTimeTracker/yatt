"""
Created by anthony on 15.10.17
echo_handler
"""
from telegram.ext import MessageHandler, Filters
from utils.handler_utils import add_timestamp, log_duration


def echo():
    return MessageHandler(Filters.text, _handle_echo)


def _handle_echo(bot, update):
    update.message.reply_text(text_to_reply(update.message.text))


@add_timestamp
@log_duration
def text_to_reply(text):
    return text
