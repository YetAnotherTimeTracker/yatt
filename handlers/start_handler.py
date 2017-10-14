"""
Created by anthony on 15.10.17
start_handler
"""
from telegram.ext import CommandHandler


COMMAND_START = 'start'


def start():
    return CommandHandler(COMMAND_START, _handle_start)


def _handle_start(bot, update):
    update.message.reply_text('Hello there!')
