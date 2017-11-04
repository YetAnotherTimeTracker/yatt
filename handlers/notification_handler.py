"""
Created by anthony on 26.10.17
notification_handler
"""
from telegram.ext import CommandHandler


COMMAND = 'q'


def notify():
    return CommandHandler(COMMAND, _handle, pass_job_queue=True)


def _handle(bot, update, job_queue):
    bot.send_message(chat_id=update.message.chat_id, text='Received message')

    args = update.message.text.split()
    seconds_till_notify = args[1]
    notification_message = ' '.join(args[2:])
    reply_text = 'Notification not found'

    if not notification_message:
        bot.send_message(chat_id=update.message.chat_id, text=reply_text)
        return

    context = {
        'chat_id': update.message.chat_id,
        'text': notification_message
    }

    try:
        bot.send_message(chat_id=update.message.chat_id, text='Setting up notification')

        seconds_as_float = float(seconds_till_notify)   # do not forget casting to float
        job_queue.run_once(callback_notifier, seconds_as_float, context=context)

    except Exception as e:
        reply_text = 'There were an error: ' + str(e)

    else:
        reply_text = 'Notification has been set up'

    update.message.reply_text(reply_text)


def callback_notifier(bot, job):
    context = job.context   # passed here via run_once(.. context=...)
    chat_id = context['chat_id']
    message = context['text']

    bot.send_message(chat_id=chat_id, text=message)
