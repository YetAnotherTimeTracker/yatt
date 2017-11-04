"""
Created by anthony on 26.10.17
queue_service
"""

# TODO make wrapper for run_once
class Notification:
    def __init__(self, bot, chat_id, seconds_till_notification, message):
        # def callback(bot, job):
        #     bot.send_message(chat_id=self.chat_id, text=self.message)

        self.bot = bot
        self.chat_id = str(chat_id)
        self.date = seconds_till_notification
        self.message = message

        queue.run_once(callback, 10)

