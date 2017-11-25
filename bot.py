"""
Created by anthony on 15.10.17
Main bot file
Only _register_ modules here (no logic)
Should just assemble and run bot
"""
from telegram.ext import Updater
import logging

from components.automata import Automata
from config import bot_config
import handlers.interaction_handler
from config.db_config import init_db
import g


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


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
    logging.info(f'> Starting {bot_config.BOT_NAME}')

    # registers handlers
    dispatcher = g.updater.dispatcher

    # handlers are invoked till the first match
    dispatcher.add_handler(handlers.interaction_handler.command_handler())

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
    init_bot()


if __name__ == '__main__':
    main()
