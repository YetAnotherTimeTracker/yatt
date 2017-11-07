from telegram.ext import CommandHandler


COMMAND_START = 'start'


def start():
    return CommandHandler(COMMAND_START, _date)

def _date(bot, update, args):
    d=parsed_datetime = utils.handler_utils.date(args)
    bot.send_message(chat_id=update.message.chat_id, text=str(d))



