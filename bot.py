"""
Created by anthony on 15.10.17
Main bot file
Only _register_ modules here (no logic)
Should just assemble and run bot
"""
from telegram.ext import Updater
from config import bot_config
from handlers import start_handler, echo_handler, task_write_handler, task_read_handler, notification_handler,date_handler
from config.db_config import init_db


print('Starting job queue')
updater = Updater(token=bot_config.BOT_API_TOKEN)
queue = updater.job_queue
print('Job queue has started')


def init_bot():
    print(f'Starting {bot_config.BOT_NAME}')

    # registers handlers
    dispatcher = updater.dispatcher

    # handlers are invoked from top to bottom till first match
    dispatcher.add_handler(start_handler.start())
    dispatcher.add_handler(notification_handler.notify())
    dispatcher.add_handler(task_write_handler.task_write())
    dispatcher.add_handler(task_read_handler.task_read())
    dispatcher.add_handler(echo_handler.echo())
    dispatcher.add_handler(date_handler.date())

    # runs
    updater.start_polling()
    print('Bot has started')

    # listens for Ctrl-C on process to stop
    updater.idle()
    print('Bot has stopped')


def main():
    # TODO handle db startup error
    init_db()
    init_bot()


if __name__ == '__main__':
    main()
