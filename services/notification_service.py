"""
Created by anthony on 17.11.17
notification_service
"""
import logging
import datetime

import g
from services import project_service, task_service
from utils import date_utils


log = logging.getLogger(__name__)


CTX_CHAT_ID = 'chat_id'
CTX_TEXT = 'text'


# TODO create_or_get or another way to remove previous notification when a new one has been set
def create_notification(chat_id, message, datetime):
    job_context = {
        CTX_CHAT_ID: chat_id,
        CTX_TEXT: message
    }
    log.info(f'Creating notification for chat ({chat_id}) on time ({datetime})')
    job = g.queue.run_once(notification_callback, datetime, context=job_context)
    return job


def notification_callback(bot, job):
    job_context = job.context  # passed here via run_once(.. context=...)

    if job_context:
        # chat id can be not int. e.g. '@username' is chat_id too
        chat_id = job_context[CTX_CHAT_ID]
        message = job_context[CTX_TEXT]
        message_wrapped = f'You have a reminder!\n{message}'

        bot.send_message(chat_id=chat_id, text=message_wrapped)
        # TODO deactivate job notification when notification is fired

    else:
        log.error('No job context found')
        raise AttributeError('No job context provided to callback')


def find_tasks_within_timedelta(task_to_check, time_delta_threshold):
    log.debug(f'checking if task is within threshold: {time_delta_threshold}')

    user_id = task_to_check.get_user_id()
    tasks = task_service.find_tasks_by_user_id(user_id)
    tasks_with_reminder = [t for t in tasks if t.get_next_remind_date() is not None
                           and t.is_task_completed() is False
                           and t.get_id() != task_to_check.get_id()]

    nearest_tasks = []
    for task in tasks_with_reminder:
        time_delta = task.get_next_remind_date() - task_to_check.get_next_remind_date()

        if abs(time_delta.total_seconds()) < time_delta_threshold.total_seconds():
            nearest_tasks.append(task)

    nearest_tasks_sorted = sorted(nearest_tasks,
                                  key=lambda t: abs(date_utils.seconds_between_tasks(t, task_to_check)))
    return nearest_tasks_sorted
