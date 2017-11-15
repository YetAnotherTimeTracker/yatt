"""
Created by anthony on 15.10.17
start_handler
"""
from telegram.ext import CommandHandler

import g
from config.state_config import State, Command
import services.state_service as ss


def start():
    return CommandHandler('start', handle)


def handle(bot, update):
    chat = update.message.chat
    try:
        curr_state = g.automata.get_state(chat.id)
        curr_context = g.automata.get_context(chat.id)

        if State.START == curr_state or State.ALL_TASKS == curr_state or State.ERROR == curr_state:

            ss.all_tasks_state(bot, update)
            g.automata.set_state(chat.id, State.ALL_TASKS)

        elif State.EDIT_DATE == curr_state:

            update.message.reply_text('Please complete date edit')
            g.automata.set_state(chat.id, State.EDIT_DATE)

        else:
            ss.error_state(bot, update, curr_context)
            g.automata.set_state(chat.id, State.ERROR)

        g.automata.get_context(chat.id).set_command(Command.START)
        update.message.reply_text(str(g.automata.get_context(chat.id)))

    except Exception as e:
        reply_on_error = f'Sorry, there were an error: {e}'
        update.message.reply_text(reply_on_error)
        return
