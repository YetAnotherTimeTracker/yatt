"""
Created by anthony on 12.11.17
state_service
"""
import datetime

from services import user_service, task_service, notification_service
from config.state_config import State, Language
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging

from components.automata import CONTEXT_TASK, CONTEXT_COMMANDS, CONTEXT_LANG
from utils import view_utils, date_utils
from components.message_source import message_source
import g


log = logging.getLogger(__name__)


def states():
    return {
        State.START: start_state,
        State.ALL_TASKS: all_tasks_state,
        State.SELECT_LANG: select_lang_state,
        State.NEW_TASK: new_task_state,
        State.VIEW_TASK: view_task_state,
        State.EDIT_DATE: edit_date_state,
        State.ERROR: error_state
    }


def start_state(bot, update, context):
    chat = update.message.chat
    user = user_service.create_or_get_user(chat)

    reply_msg = 'Hello'
    if user:
        reply_msg += ', ' + user.get_first_name()

    update.message.reply_text(reply_msg)


def all_tasks_state(bot, update, context):
    chat = update.effective_chat
    chat_id = chat.id

    user = user_service.create_or_get_user(chat)
    user_tasks = task_service.find_tasks_by_user_id(user.get_id())
    lang = context[CONTEXT_LANG]
    tasks_to_show = [f'[{t.get_id()}] {t.get_description()}' for t in user_tasks]

    first_name = user.get_first_name()
    if 0 == len(tasks_to_show):

        bot.send_message(chat_id=chat_id,
                         text=message_source[lang]['no_tasks_yet'])
        update.message.reply_text(message_source[lang]['write_me'])

    else:
        keyboard = []

        for task_as_string, task_object  in zip(tasks_to_show,user_tasks):
            keyboard.append([InlineKeyboardButton(str(task_as_string), callback_data=str(task_object.get_id()))])
        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(chat_id=chat_id,
                         text=message_source[lang]['your_tasks'].format(first_name),reply_markup=reply_markup)


def select_lang_state(bot, update, context):
    chat = update.message.chat
    user = user_service.create_or_get_user(chat)

    reply_msg = 'Hello'
    if user:
        reply_msg += ', ' + user.get_first_name()
    reply_msg += "\nSelect language:"
    keyboard = [
        [InlineKeyboardButton("Русский", callback_data=Language.RUS.value),
         InlineKeyboardButton("English", callback_data=Language.ENG.value)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(reply_msg, reply_markup=reply_markup)


def new_task_state(bot, update, context):
    chat = update.message.chat
    lang = context[CONTEXT_LANG]
    new_task = task_service.create_task(update)

    if g.test_mode:
        log.debug(f'Automatically setting reminder time for task {new_task.get_id()}')
        d1 = datetime.datetime.now()
        d2 = datetime.datetime.now() + datetime.timedelta(days=1)
        parsed_datetime = date_utils.random_date(d1, d2)

        new_task.set_next_remind_date(parsed_datetime)
        task_service.update_task(new_task)

    if new_task:
        context[CONTEXT_TASK] = new_task
        reply_on_success = message_source[lang]['task_created'].format(new_task.get_id())

        user = user_service.find_one_by_user_id(chat.id)
        if user:
            reply_on_success = user.get_first_name() + ', ' + reply_on_success

        update.message.reply_text(reply_on_success.capitalize())


def view_task_state(bot, update, context):
    args = update.message.text.split()
    task_id = args[1]
    lang = context[CONTEXT_LANG]
    chat = update.message.chat
    user = user_service.create_or_get_user(chat)

    task = task_service.find_task_by_id_and_user_id(task_id, user.get_id())

    # TODO handle if task is completed/enabled notifications/deleted
    if task:
        context[CONTEXT_TASK] = task

        task_descr = task.get_description()
        update.message.reply_text(f'[{task_id}]: {task_descr}')

    else:
        update.message.reply_text(message_source[lang]['cant_find_task'].format(task.get_id()))


def edit_date_state(bot, update, context):
    user_id = update.message.chat.id
    args = update.message.text.split()
    datetime_args = args[1:]
    latest_task = context[CONTEXT_TASK]
    lang = context[CONTEXT_LANG]

    err_cause = None
    if latest_task:

        parsed_datetime = None
        if g.dev_mode or g.test_mode:
            seconds = int(datetime_args[0]) or 10
            parsed_datetime = datetime.datetime.now() + datetime.timedelta(seconds=seconds)

        else:
            parsed_datetime = date_utils.parse_date_msg(datetime_args)

        latest_task.set_next_remind_date(parsed_datetime)
        task_service.update_task(latest_task)
        update.message.reply_text(message_source[lang]['set_date'].format(parsed_datetime))

        # TODO add responseBuilder that can be used this way: rb.append(x), rb.appendNewLine(x)
        update.message.reply_text(view_utils.render_task_basic(latest_task))

        # find if reminder intersects with another tasks
        time_delta_threshold = datetime.timedelta(hours=8)
        nearest_tasks = task_service.find_tasks_within_timedelta(latest_task, time_delta_threshold)
        if 0 != len(nearest_tasks):

            tasks_to_show = [view_utils.render_task_with_timedelta(t, latest_task) for t in nearest_tasks]
            tasks_to_show = tasks_to_show[0:3]
            update.message.reply_text(f'Don\' forget that You already have ' +
                                      'task' if 1 == len(nearest_tasks) else 'tasks' +
                                      f'assigned near that time:\n' + '\n'.join(tasks_to_show) +
                                      '\nIf you want to change reminder time, just write it :)')
        return

    else:
        err_cause = 'Task does not exist'

    if err_cause:
        log.error(err_cause)
        update.message.reply_text(f'Sorry, I could not find that task')


def error_state(bot, update, context):
    lang = context[CONTEXT_LANG]
    latest_task = context[CONTEXT_TASK]

    if latest_task:
        command_trace = [c.name for c in context[CONTEXT_COMMANDS]]
        update.message.reply_text(message_source[lang]['error'].format(latest_task.get_id(), command_trace))

    else:
        log.warning("No task in context found")
