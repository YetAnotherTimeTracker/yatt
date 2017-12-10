"""
Created by anthony on 12.11.17
state_service
"""
import datetime

from services import user_service, task_service, notification_service
from config.state_config import State, Language, CallbackData, Action
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging

from components.automata import CONTEXT_TASK, CONTEXT_COMMANDS, CONTEXT_LANG
from components.keyboard_builder import KeyboardBuilder as Kb
from utils import view_utils, date_utils
from components.message_source import message_source
import g
from utils.handler_utils import is_callback, deserialize_data

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
    lang = context[CONTEXT_LANG]

    action = None
    if is_callback(update):
        deserialized = deserialize_data(update.callback_query.data)
        action = deserialized[CallbackData.ACTION]

    else:
        pass

    user = user_service.create_or_get_user(chat)
    user_id = user.get_id()
    tasks = []

    if action is Action.LIST_ALL:
        tasks = task_service.find_tasks_by_user_id(user_id)

    elif action is Action.LIST_UPCOMING:
        tasks = task_service.find_upcoming_tasks_by_user_id(user_id)

    elif action is Action.LIST_COMPLETED:
        tasks = task_service.find_completed_tasks_by_user_id(user_id)

    else:
        tasks = task_service.find_tasks_by_user_id(user.get_id())

    if 0 == len(tasks):
        bot.send_message(chat_id=chat_id,
                         text=message_source[lang]['state.all_tasks.no_tasks_yet'])

    else:
        text = message_source[lang]['state.all_tasks.your_tasks']
        if user and 'none' != user.get_first_name().lower():
            text = user.get_first_name() + ', ' + text

        else:
            text = text.capitalize()

        markup = Kb.all_tasks_buttons(tasks)
        bot.send_message(chat_id=chat_id,
                         text=text,
                         reply_markup=markup)


def select_lang_state(bot, update, context):
    chat = update.effective_chat
    user = user_service.create_or_get_user(chat)
    lang = context[CONTEXT_LANG]

    text = message_source[lang]['state.select_lang']
    if user and 'none' != user.get_first_name().lower():
        text = user.get_first_name() + ', ' + text

    else:
        text = text.capitalize()

    lang = context[CONTEXT_LANG]
    markup = Kb.select_lang_buttons(lang)
    bot.send_message(chat_id=chat.id,
                     text=text,
                     reply_markup=markup)


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
    chat = update.effective_chat
    chat_id = chat.id
    lang = context[CONTEXT_LANG]

    task_id = None
    action = None
    if is_callback(update):
        deserialized = deserialize_data(update.callback_query.data)
        task_id = deserialized[CallbackData.DATA]
        action = deserialized[CallbackData.ACTION]

    else:
        args = update.message.text.split()
        task_id = args[1]

    user = user_service.create_or_get_user(chat)
    task = task_service.find_task_by_id_and_user_id(task_id, user.get_id())

    # TODO handle if task is completed/enabled notifications/deleted
    if task:
        reply_text = task.get_description()

        if action is Action.TASK_MARK_AS_DONE:
            task.mark_as_completed()
            reply_text = message_source[lang]['btn.view_task.mark_as_done.result']

        elif action is Action.TASK_DISABLE:
            task.mark_as_disabled()
            reply_text = message_source[lang]['btn.view_task.disable_notify.result']

        elif action is Action.TASK_DELETE:
            task.mark_as_inactive()
            reply_text = message_source[lang]['btn.view_task.delete_task.result']

        elif action is Action.TASK_VIEW:
            # It's not callback, then just render the state
            reply_text = task.get_description()

        # update task
        task_service.update_task(task)

        # set updated task to context
        context[CONTEXT_TASK] = task

        view_task_buttons = Kb.view_task_buttons(lang, task_id)
        bot.send_message(chat_id=chat_id,
                         text=reply_text,
                         reply_markup=view_task_buttons)

    else:
        bot.send_message(chat_id=chat_id,
                         text=message_source[lang]['state.view_task.not_found'])


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
