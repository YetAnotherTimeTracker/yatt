"""
Created by anthony on 12.11.17
edit_date_handler
"""
from telegram.ext import CommandHandler

import g
from config.state_config import State
import services.state_service as ss


def edit_date():
    return CommandHandler('date', handle)


def handle(bot, update):
    chat = update.message.chat
    try:
        curr_state = g.automata.get_state(chat.id)

        if State.START == curr_state:

            ss.start_state(bot, update)
            g.automata.set_state(chat.id, State.START)

        elif State.NEW_TASK == curr_state or State.VIEW_TASK == curr_state or State.EDIT_DATE == curr_state:

            ss.edit_date_state(bot, update, context={})
            g.automata.set_state(chat.id, State.EDIT_DATE)

        else:
            update.message.reply_text('Error!')
            g.automata.set_state(chat.id, State.ERROR)

    except Exception as e:
        reply_on_error = f'Sorry, there were an error: {e}'
        update.message.reply_text(reply_on_error)
