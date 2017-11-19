"""
Created by anthony on 17.11.17
notification_service
"""
import g


CTX_CHAT_ID = 'chat_id'
CTX_TEXT = 'text'


# TODO create_or_get or another way to remove previous notification when a new one has been set
def create_notification(chat_id, message, datetime):
    def notification_callback(bot, job):
        job_context = job.context  # passed here via run_once(.. context=...)

        if job_context:
            # chat id can be not int. e.g. '@username' is chat_id too
            chat_id = job_context[CTX_CHAT_ID]
            message = job_context[CTX_TEXT]

            bot.send_message(chat_id=chat_id, text=message)
            # TODO deactivate job notification when notification is fired

    job_context = {
        CTX_CHAT_ID: chat_id,
        CTX_TEXT: message
    }
    job = g.queue.run_once(notification_callback, datetime, context=job_context)
    return job
