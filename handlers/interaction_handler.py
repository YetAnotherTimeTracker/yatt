"""
Created by anthony on 15.10.17
start_handler
"""
from telegram.ext import MessageHandler

import g
from components.filter import command_filter
from config.state_config import CommandType, CommandAliases
from services import state_service
from utils.handler_utils import get_command_type


def command_handler():
    return MessageHandler(command_filter, handle)


def handle(bot, update):
    try:
        chat = update.message.chat
        text = update.message.text

        curr_state = g.automata.get_state(chat.id)
        curr_context = g.automata.get_context(chat.id)
        curr_command = get_command_type(text)

        state = g.automata.get_transition(curr_state, curr_command)
        update.message.reply_text('rendering state: ' + state.name)

        handler = state_service.states()[state]
        handler(bot, update, curr_context)

        g.automata.set_state(chat.id, state)
        g.automata.get_context(chat.id).add_command(curr_command)


        update.message.reply_text(str(g.automata.get_context(chat.id)))

    except Exception as e:
        reply_on_error = f'Sorry, there were an error: {e}'
        update.message.reply_text(reply_on_error)
        return
