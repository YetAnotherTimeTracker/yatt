"""
Created by anthony on 15.10.17
echo_handler
"""
from telegram.ext import MessageHandler, Filters

import g
from config.state_config import State, Command
import services.state_service as ss


def echo():
    return MessageHandler(Filters.text, _handle)


def _handle(bot, update):
    chat = update.message.chat
    try:
        curr_state = g.automata.get_state(chat.id)

        if State.START == curr_state:

            ss.start_state(bot, update)

            # update.message.reply_text('Haven\'t we met yet?')
            g.automata.set_state(chat.id, State.START)
            # g.automata.set_context(chat.id, {ENC_NUM: 0})

        else:
            ss.new_task_state(bot, update)
            g.automata.set_state(chat.id, State.NEW_TASK)

        g.automata.get_context(chat.id).set_command(Command.ECHO)
        update.message.reply_text(str(g.automata.get_context(chat.id)))

    except Exception as e:
        reply_on_error = f'Sorry, there were an error: {e}'
        update.message.reply_text(reply_on_error)
        return
