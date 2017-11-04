"""
Created by anthony on 26.10.17
queue_service
"""
from telegram.ext import JobQueue, Job
# from bot import queue


class Notification:
    def __init__(self, bot, chat_id, seconds_till_notification, message):
        # def callback(bot, job):
        #     bot.send_message(chat_id=self.chat_id, text=self.message)

        def callback(bot, job):
            bot.send_message(chat_id='316956601', text='hallo')

        self.bot = bot
        self.chat_id = str(chat_id)
        self.date = seconds_till_notification
        self.message = message

        queue.run_once(callback, 10)

