"""
Created by anthony on 17.11.17
notification_service
"""
import logging

import datetime

import g
from components.automata import CONTEXT_LANG
from components.message_source import message_source
from components.keyboard_builder import KeyboardBuilder as kb
from services import task_service

log = logging.getLogger(__name__)


PAYLOAD_CHAT_ID = 'payload_chat_id'
PAYLOAD_TEXT = 'payload_text'
PAYLOAD_TASK_ID = 'payload_task_id'


# TODO create_or_get or another way to remove previous notification when a new one has been set
def create_notification(chat_id, task):
    payload = {
        PAYLOAD_CHAT_ID: chat_id,
        PAYLOAD_TASK_ID: task.get_id(),
        PAYLOAD_TEXT: task.get_description()
    }
    remind_date = task.get_next_remind_date()
    log.info(f'Creating notification for chat ({chat_id}) on time ({remind_date})')
    job = g.queue.run_once(callback=notification_callback, when=remind_date, context=payload)
    return job


def notification_callback(bot, job):
    payload = job.context  # passed here via run_once(.. context=...)

    if payload:
        # chat id can be not int. e.g. '@username' is chat_id too
        chat_id, task_id, text = map(payload.get, (PAYLOAD_CHAT_ID, PAYLOAD_TASK_ID, PAYLOAD_TEXT))

        task = task_service.find_task_by_id_and_user_id(task_id, chat_id)
        if task.is_task_enabled() is False or task.is_task_completed():
            log.info(f'Notification for task {task_id} is disabled. Skipping')
            return

        message_wrapped = f'You have a reminder!\n{text}'

        # create custom keyboard for user to be able to mark task as completed
        context = g.automata.get_context(chat_id)
        lang = context[CONTEXT_LANG]
        button_map = [
            {
                kb.LABEL: message_source[lang]['btn.mark_as_done'],
                kb.DATA: str(task_id),
                kb.ACTION: 'mark_as_done'
            },
            [
                {
                    kb.LABEL: message_source[lang]['btn.disable_notify'],
                    kb.DATA: str(task_id),
                    kb.ACTION: 'disable'
                },
                {
                    kb.LABEL: message_source[lang]['btn.delete_task'],
                    kb.DATA: str(task_id),
                    kb.ACTION: 'delete'
                }
            ]
        ]
        markup = kb.inline_keyboard(button_map)

        bot.send_message(chat_id=chat_id, text=message_wrapped, reply_markup=markup)
        # TODO deactivate job notification when notification is fired

    else:
        log.error('No payload found in notification callback')


def load_tasks_to_queue():
    """
    Gets all tasks that will be fired in future and sets them to job queue
    This method is originally made to not forget notifications in queue when bot is restarted
    """
    all_tasks = task_service.find_all_tasks()
    now = datetime.datetime.now()
    tasks_not_yet_fired = [t for t in all_tasks if t.get_next_remind_date() is not None
                           and now < t.get_next_remind_date()]

    log.info(f'Creating notifications for {len(tasks_not_yet_fired)} tasks')
    for t in tasks_not_yet_fired:
        create_notification(t.get_user_id(), t)


    return tasks_not_yet_fired
