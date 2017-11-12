"""
Created by anthony on 15.10.17
Main bot file
Only _register_ modules here (no logic)
Should just assemble and run bot
"""
import inspect

from telegram.ext import Updater
from config import bot_config
import handlers.start_handler, handlers.echo_handler, handlers.task_write_handler, \
    handlers.all_tasks_handler, handlers.notification_handler, \
    handlers.view_task_handler, handlers.edit_date_handler
from config.db_config import init_db
from config.state_config import Automata
import g


def init_job_queue():
    print('> Starting job queue')
    g.updater = Updater(token=bot_config.TOKEN)
    g.queue = g.updater.job_queue
    print('Job queue has started')


def init_automata():
    print('> Starting state automata')
    g.automata = Automata()
    print('State automata has started')


def init_bot():
    print(f'> Starting {bot_config.BOT_NAME}')

    # registers handlers
    dispatcher = g.updater.dispatcher

    # handlers are invoked from top to bottom till first match
    dispatcher.add_handler(handlers.start_handler.start())
    dispatcher.add_handler(handlers.view_task_handler.view_task())
    dispatcher.add_handler(handlers.edit_date_handler.edit_date())
    dispatcher.add_handler(handlers.notification_handler.notify())
    dispatcher.add_handler(handlers.task_write_handler.task_write())
    dispatcher.add_handler(handlers.all_tasks_handler.all_tasks())
    dispatcher.add_handler(handlers.echo_handler.echo())

    # runs
    g.updater.start_polling()
    print('Bot has started')

    # listens for Ctrl-C on process to stop
    g.updater.idle()
    print('Bot has stopped')


def main():
    # TODO handle startup error
    init_db()
    init_job_queue()
    init_automata()
    print(len(inspect.stack()))

    init_bot()



if __name__ == '__main__':
    main()
