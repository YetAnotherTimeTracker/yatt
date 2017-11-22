"""
Created by anthony on 15.10.17
start_handler
"""
from telegram.ext import MessageHandler

import g
from components.automata import CONTEXT_COMMANDS, CONTEXT_TASK
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

        # get all params that needed to render state
        curr_state = g.automata.get_state(chat.id)
        curr_context = g.automata.get_context(chat.id)
        curr_command = get_command_type(text)

        # find out state to be rendered
        state = g.automata.get_transition(curr_state, curr_command)
        update.message.reply_text('rendering state: ' + state.name)

        # get state from service and render
        handler = state_service.states()[state]
        handler(bot, update, curr_context)

        # update params
        g.automata.set_state(chat.id, state)
        curr_context[CONTEXT_COMMANDS].append(curr_command)


        context_commands = [c.name for c in curr_context[CONTEXT_COMMANDS]]
        context_task = curr_context[CONTEXT_TASK].get_id() if curr_context[CONTEXT_TASK] else '-'
        update.message.reply_text(f'Latest task: {context_task}\nLatest commands: {context_commands}')

    except Exception as e:
        update.message.reply_text(f'Sorry, there were an error: {e}')
        return
