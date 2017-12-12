"""
Created by anthony on 12.11.17
state_service
"""
import datetime
from emoji import emojize
from telegram import ParseMode

from services import user_service, task_service
from config.state_config import State, Language, CallbackData, Action
import logging

from components.automata import CONTEXT_TASK, CONTEXT_COMMANDS, CONTEXT_LANG
from components.keyboard_builder import KeyboardBuilder as Kb
from utils import view_utils, date_utils
from components.message_source import message_source
import g
from utils.handler_utils import is_callback, deserialize_data
from utils.view_utils import concat_username

log = logging.getLogger(__name__)


def states():
    return {
        State.START: start_state,
        State.ALL_TASKS: all_tasks_state,
        State.SELECT_LANG: select_lang_state,
        State.NEW_TASK: new_task_state,
        State.VIEW_TASK: view_task_state,
        State.EDIT_DATE: edit_date_state,
        State.EMPTY: empty_state,
        State.ERROR: error_state,
    }


def start_state(bot, update, context):
    chat = update.effective_chat
    chat_id = chat.id
    user = user_service.create_or_get_user(chat)

    if is_callback(update):
        deserialized = deserialize_data(update.callback_query.data)
        action = deserialized[CallbackData.ACTION]

        if action is Action.SELECTED_LANG:
            lang = deserialized[CallbackData.DATA]
            context[CONTEXT_LANG] = Language(lang)

    lang = context[CONTEXT_LANG]
    welcome_text = message_source[lang]['state.start_state.welcome']
    rocket_emoji = ':rocket: *'
    welcome_text = concat_username(rocket_emoji, user, ', ' + welcome_text)

    num_all, num_upcoming, num_completed = task_service.find_stats_for_user(chat_id)
    bot_ver = 13    # because why not? :)
    welcome_text = welcome_text.format(num_upcoming, num_completed, num_all, bot_ver)

    buttons = Kb.start_state_buttons(lang)
    bot.send_message(chat_id=chat_id,
                     text=emojize(welcome_text, use_aliases=True),
                     parse_mode=ParseMode.MARKDOWN,
                     reply_markup=buttons)


def all_tasks_state(bot, update, context):
    chat = update.effective_chat
    chat_id = chat.id
    lang = context[CONTEXT_LANG]

    action = None
    if is_callback(update):
        deserialized = deserialize_data(update.callback_query.data)
        action = deserialized[CallbackData.ACTION]

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
                         text=emojize(message_source[lang]['state.all_tasks.no_tasks_yet'], use_aliases=True))

    else:
        text = message_source[lang]['state.all_tasks.your_tasks']
        text = concat_username('', user, ', ' + text)

        markup = Kb.all_tasks_buttons(tasks)
        bot.send_message(chat_id=chat_id,
                         text=emojize(text, use_aliases=True),
                         reply_markup=markup)


def select_lang_state(bot, update, context):
    chat = update.effective_chat
    chat_id = chat.id

    user = user_service.create_or_get_user(chat)

    action = None
    if is_callback(update):
        deserialized = deserialize_data(update.callback_query.data)
        action = deserialized[CallbackData.ACTION]

    globe_emoji = ':earth_africa: '
    # find out what are we doing now? selecting lang or just showing available langs
    text = None
    if action is Action.SELECTED_LANG:
        deserialized = deserialize_data(update.callback_query.data)
        lang_string = deserialized[CallbackData.DATA]
        lang = Language(lang_string)
        context[CONTEXT_LANG] = lang
        text = message_source[lang]['btn.select_lang.' + lang_string + '.result']
        buttons = Kb.start_state_buttons(lang)

    elif action is Action.VIEW_LANG:
        # It's callback. nevertheless just show available langs
        lang = context[CONTEXT_LANG]
        text = message_source[lang]['state.select_lang']
        text = concat_username(globe_emoji + ' *', user, ', ' + text)

        buttons = Kb.select_lang_buttons(lang)

    else:
        # It's not callback. just show available langs
        lang = context[CONTEXT_LANG]
        text = message_source[lang]['state.select_lang']
        text = concat_username(globe_emoji + ' *', user, ', ' + text)

        buttons = Kb.select_lang_buttons(lang)

    bot.send_message(chat_id=chat_id,
                     text=emojize(text, use_aliases=True),
                     parse_mode=ParseMode.MARKDOWN,
                     reply_markup=buttons)


def new_task_state(bot, update, context):
    chat = update.effective_chat
    chat_id = chat.id
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

        project_buttons = Kb.select_project_buttons(lang)

        bot.send_message(chat_id=chat_id,
                         text=emojize(reply_on_success, use_aliases=True),
                         reply_markup=project_buttons)


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
                         text=emojize(reply_text, use_aliases=True),
                         reply_markup=view_task_buttons)

    else:
        bot.send_message(chat_id=chat_id,
                         text=emojize(message_source[lang]['state.view_task.not_found'], use_aliases=True))


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


def empty_state(bot, update, context):
    pass


def error_state(bot, update, context):
    chat = update.effective_chat
    chat_id = chat.id

    lang = context[CONTEXT_LANG]
    latest_task = context[CONTEXT_TASK]

    if latest_task:
        command_trace = [c.name for c in context[CONTEXT_COMMANDS]]
        bot.send_message(chat_id=chat_id,
                         text=emojize(message_source[lang]['error'].format(latest_task.get_id(), command_trace)),
                         use_aliases=True)

    else:
        log.warning("No task in context found")
