"""
Created by anthony on 17.11.17
notification_service
"""
import g
import logging


log = logging.getLogger(__name__)


CTX_CHAT_ID = 'chat_id'
CTX_TEXT = 'text'


# TODO create_or_get or another way to remove previous notification when a new one has been set
def create_notification(chat_id, message, datetime):
    job_context = {
        CTX_CHAT_ID: chat_id,
        CTX_TEXT: message
    }
    log.info(f'Creating job scheduled to {datetime} for chat {chat_id}')
    job = g.queue.run_once(notification_callback, datetime, context=job_context)
    return job


def notification_callback(bot, job):
    job_context = job.context  # passed here via run_once(.. context=...)

    if job_context:
        # chat id can be not int. e.g. '@username' is chat_id too
        chat_id = job_context[CTX_CHAT_ID]
        message = job_context[CTX_TEXT]
        message_wrapped = f'You have a reminder!\n{message}'

        log.info(f'Sending remind msg to chat ({chat_id}) of: {message}')
        bot.send_message(chat_id=chat_id, text=message_wrapped)
        # TODO deactivate job notification when notification is fired

    else:
        # TODO change to another one since i dont know what else python has
        raise ValueError('Job context is None')
