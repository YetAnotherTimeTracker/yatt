from telegram.ext import CommandHandler


COMMAND_START = 'date'


def start():
    return CommandHandler(COMMAND_START, _date)

def _date(bot, update, args):
    pars_date = utils.handler_utils.date(args)
    bot.send_message(chat_id=update.message.chat_id, text=str(pars_date))



