"""
Created by anthony on 26.10.17
notification_handler
"""
from telegram.ext import CommandHandler
import uuid
from models.task import Task
from services import queue_service
from services.queue_service import CallbackJob
from bot import *


COMMAND = 'q'


def notify():
    return CommandHandler(COMMAND, _handle)


def _handle(bot, update):

    text = update.message.text
    args = text.split()
    seconds_till_notify = args[1]
    notification_message = ' '.join(args[2:])

    reply_text = 'Notification has been created'

    notification = CallbackJob(notification_message, str(uuid.uuid4()))
    try:
        queue.add_job(notification, seconds_till_notify)
        print('job added')

    except Exception as e:
        reply_text = 'There were an error'

    update.message.reply_text(reply_text)
