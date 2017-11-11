"""
Created by anthony on 15.10.17
Main bot file
Only _register_ modules here (no logic)
Should just assemble and run bot
"""
from telegram.ext import Updater
from config import bot_config
from handlers import start_handler, echo_handler, task_write_handler, task_read_handler, notification_handler
from config.db_config import init_db
from services.state_service import Automata


def init_job_queue():
    print('> Starting job queue')
    updater = Updater(token=bot_config.TOKEN)
    queue = updater.job_queue
    print('Job queue has started')
    return updater, queue


def init_automata():
    print('> Starting state automata')
    automata = Automata()
    print('State automata has started')
    return automata


updater, queue = init_job_queue()
automata = init_automata()


def init_bot():
    print(f'> Starting {bot_config.BOT_NAME}')

    # registers handlers
    dispatcher = updater.dispatcher

    # handlers are invoked from top to bottom till first match
    dispatcher.add_handler(start_handler.start())
    dispatcher.add_handler(notification_handler.notify())
    dispatcher.add_handler(task_write_handler.task_write())
    dispatcher.add_handler(task_read_handler.task_read())
    dispatcher.add_handler(echo_handler.echo())

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
