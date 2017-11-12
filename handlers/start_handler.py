"""
Created by anthony on 15.10.17
start_handler
"""
from telegram.ext import CommandHandler

from bot import automata
from services import user_service


COMMAND_START = 'start'


def start():
    return CommandHandler(COMMAND_START, _handle_start)


ENC_NUM = 'encounter_num'

def _handle_start(bot, update):
    reply_msg = 'Hello'
    chat = update.message.chat
    try:
        if 0 == automata.get_state(chat.id):
            print('curr state: 0')
            update.message.reply_text('Haven\'t we met yet?')
            automata.set_state(chat.id, 1)
            automata.set_context(chat.id, {ENC_NUM: 0})

        elif 1 == automata.get_state(chat.id):
            automata.set_state(chat.id, 2)
            enc_num_value = automata.get_context(chat.id)[ENC_NUM] + 1
            automata.set_context(chat.id, {ENC_NUM: enc_num_value})
            update.message.reply_text(f'Oh, I know you. We have me for {enc_num_value} times')

        elif 2 == automata.get_state(chat.id):
            automata.set_state(chat.id, 3)
            update.message.reply_text('Hello my dear friend')
            enc_num_value = automata.get_context(chat.id)[ENC_NUM] + 1
            automata.set_context(chat.id, {ENC_NUM: enc_num_value})

        else:
            enc_num_value = automata.get_context(chat.id)[ENC_NUM] + 1
            automata.set_context(chat.id, {ENC_NUM: enc_num_value})
            update.message.reply_text(f'Hi! It\'s  the {enc_num_value} we meet :)')

        user = user_service.create_or_get_user(chat)

        if user:
            reply_msg += ', ' + user.get_first_name()

        #update.message.reply_text(reply_msg)

    except Exception as e:
        update.message.reply_text(reply_msg)
