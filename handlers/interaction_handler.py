"""
Created by anthony on 15.10.17
start_handler
"""
import logging
import telegram
from telegram.ext import MessageHandler, Filters

import g
from components.automata import CONTEXT_COMMANDS, CONTEXT_TASK
from components.filter import command_filter
from services import state_service
from utils.handler_utils import get_command_type


log = logging.getLogger(__name__)


def command_handler():
    return MessageHandler(Filters.all, handle)


def handle(bot, update):
    bot.send_chat_action(chat_id=update.message.chat.id, action=telegram.ChatAction.TYPING)
    try:
        chat = update.message.chat
        text = update.message.text
        log.info(f'Incoming message from {chat.username} ({chat.id})): {text}')

        if not command_filter.known_command(text):
            reply_on_unknown(bot, update)
            return

        # get all params needed to render state
        curr_state = g.automata.get_state(chat.id)
        curr_context = g.automata.get_context(chat.id)
        curr_command = get_command_type(text)
        log.info(f'curr_state: {curr_state}, curr_command: {curr_command}')


        # find out state to be rendered
        state = g.automata.get_transition(curr_state, curr_command)
        if g.dev_mode:
            update.message.reply_text(f'state: {curr_state.name} ({curr_state.value})\n'
                                      f'cmd: {curr_command.name} ({curr_command.value})\n'
                                      f'new state: {state.name} ({state.value})')

        # get state from service and render
        handler = state_service.states()[state]
        log.info(f'rendering state: {handler.__name__}')
        handler(bot, update, curr_context)

        # update params
        log.info(f'Updating state to: {state}')
        g.automata.set_state(chat.id, state)
        log.info(f'Updating context with command: {curr_command}')
        curr_context[CONTEXT_COMMANDS].append(curr_command)


        if g.dev_mode:
            print_dev_info(bot, update, curr_context)

    except Exception as e:
        log.error('Error has been caught in handler: ', e)
        update.message.reply_text(f'Sorry, there were an error: {e}')
        return

    else:
        log.info('Successfully handled')


def reply_on_unknown(bot, update):
    log.info('Replying on unknown command')
    reply_text = 'Go fuck yourself, please'
    bot.send_message(chat_id=update.message.chat.id,
                     text='Go <b>fuck</b> <i>yourself</i>, please',
                     parse_mode=telegram.ParseMode.HTML)


def print_dev_info(bot, update, curr_context):
    context_commands = [c.name for c in curr_context[CONTEXT_COMMANDS]]
    context_task = curr_context[CONTEXT_TASK].get_id() if curr_context[CONTEXT_TASK] else '-'
    update.message.reply_text(f'Latest task: {context_task}\nLatest commands: {context_commands}')
