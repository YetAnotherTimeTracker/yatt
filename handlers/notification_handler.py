"""
Created by anthony on 26.10.17
notification_handler
"""
from telegram.ext import CommandHandler
import uuid
from models.task import Task
from services import queue_service
from services.queue_service import Notification
import bot as bot_module


COMMAND = 'q'


def notify():
    return CommandHandler(COMMAND, _handle, pass_job_queue=True)


def _handle(bot, update, job_queue):
    bot.send_message(chat_id=update.message.chat_id, text='Received message')

    text = update.message.text
    args = text.split()
    seconds_till_notify = args[1]
    notification_message = ' '.join(args[2:])

    reply_text = 'Notification has been created'
    #
    # def callback(bot, job):
    #     bot.send_message(chat_id='316956601', text='hallo')
    try:
        # notification = Notification(bot, update.message.chat_id, seconds_till_notify, notification_message)
        # print('notification has been scheduled')
        job_queue.run_once(callback_notifier, 5, context=update.message.chat_id)
        bot.send_message(chat_id=update.message.chat_id, text='Notification has been set')

    except Exception as e:
        reply_text = 'There were an error' + str(e)

    update.message.reply_text(reply_text)


def callback_notifier(bot, job):
    context = job.context   # update.message is passed here via run_once(.. context=...)
    bot.send_message(chat_id=context, text='Notifying u')

#
# def callback_timer(bot, update, job_queue):
#     bot.send_message(chat_id='316956601', text='Setting timer')
#
#     job_queue.run_once(callback_notifier, 5, context=update.message.chat_id)
