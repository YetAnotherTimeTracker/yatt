from telegram.ext import CommandHandler
from utils.handler_utils import parse_date_msg

COMMAND_START = 'date'


def date():
    return CommandHandler(COMMAND_START, _handle_date, pass_args=True)

def _handle_date(bot, update, args):

    parse_date_msg(args)
    pars_date = parse_date_msg(args)

    bot.send_message(chat_id=update.message.chat_id, text='date set at '+str(pars_date))



