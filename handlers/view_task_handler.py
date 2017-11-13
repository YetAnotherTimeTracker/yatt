"""
Created by anthony on 12.11.17
view_task_handler
"""
from telegram.ext import CommandHandler

import g
from config.state_config import State, Command
import services.state_service as ss


def view_task():
    return CommandHandler('task', handle)


def handle(bot, update):
    chat = update.message.chat
    args = update.message.text.split()
    task_id = args[1]
    try:
        curr_state = g.automata.get_state(chat.id)

        if State.START == curr_state:

            ss.start_state(bot, update)
            g.automata.set_state(chat.id, State.VIEW_TASK)
            # g.automata.set_context(chat.id, {ENC_NUM: 0})

        else:
            ss.view_task_state(bot, update)
            g.automata.set_state(chat.id, State.VIEW_TASK)
            g.automata.get_context(chat.id).set_task(task_id)

        g.automata.get_context(chat.id).set_command(Command.TASK)
        update.message.reply_text(str(g.automata.get_context(chat.id)))

    except Exception as e:
        reply_on_error = f'Sorry, there were an error: {e}'
        update.message.reply_text(reply_on_error)
        return
