"""
Created by anthony on 18.10.17
task_read_handler
"""
from telegram.ext import CommandHandler

import g
from config.state_config import State, Command
import services.state_service as ss


def all_tasks():
    return CommandHandler('all', handle)


def handle(bot, update):
    chat = update.message.chat
    try:
        curr_state = g.automata.get_state(chat.id)

        if State.START == curr_state:

            ss.start_state(bot, update)
            g.automata.set_state(chat.id, State.START)

        else:
            ss.all_tasks_state(bot, update)
            g.automata.set_state(chat.id, State.ALL_TASKS)

        g.automata.get_context(chat.id).set_command(Command.ALL)
        update.message.reply_text(str(g.automata.get_context(chat.id)))

    except Exception as e:
        reply_on_error = f'Sorry, there were an error: {e}'
        update.message.reply_text(reply_on_error)
        return
