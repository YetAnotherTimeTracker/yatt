"""
Created by anthony on 17.11.17
notification_service
"""
import logging

import g
from components.automata import CONTEXT_LANG
from components.message_source import message_source
from components.keyboard_builder import KeyboardBuilder as kb


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
        message_wrapped = f'You have a reminder!\n{text}'

        # create custom keyboard for user to be able to mark task as completed
        context = g.automata.get_context(chat_id)
        lang = context[CONTEXT_LANG]
        button_map = [
            {
                kb.LABEL: message_source[lang]['btn.mark_as_done'],
                kb.DATA: str(task_id)
            },
            {
                kb.LABEL: message_source[lang]['btn.delete_task'],
                kb.DATA: str(task_id)
            }
        ]
        markup = kb.inline_horizontal(button_map)

        bot.send_message(chat_id=chat_id, text=message_wrapped, reply_markup=markup)
        # TODO deactivate job notification when notification is fired

    else:
        log.error('No payload found in notification callback')
