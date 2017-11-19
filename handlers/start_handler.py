"""
Created by anthony on 15.10.17
start_handler
"""
from telegram.ext import CommandHandler

import g
from config.state_config import State, Command
import services.state_service as ss
from services import state_service


def start():
    return CommandHandler('start', handle)


def handle(bot, update):
    chat = update.message.chat
    try:
        curr_state = g.automata.get_state(chat.id)
        curr_context = g.automata.get_context(chat.id)
        curr_command = Command.START

        state = g.automata.get_transition(curr_state, curr_command)
        handler = state_service.states()[state]
        handler(bot, update, curr_context)

        g.automata.set_state(chat.id, State.ALL_TASKS)
        g.automata.get_context(chat.id).set_command(Command.START)

        # if mode is development:
        #update.message.reply_text(str(g.automata.get_context(chat.id)))

    except Exception as e:
        reply_on_error = f'Sorry, there were an error: {e}'
        update.message.reply_text(reply_on_error)
        return
