"""
Created by anthony on 12.11.17
state_service
"""
from components.automata import CONTEXT_TASK, CONTEXT_COMMANDS, CONTEXT_LANG
from services import user_service, task_service
from config.state_config import State, Language
import datetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils import handler_utils
from components.message_source import message_source
import g


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
    chat = update.message.chat
    user = user_service.create_or_get_user(chat)
    user_tasks = task_service.find_tasks_by_user_id(user.get_id())
    lang = context[CONTEXT_LANG]
    tasks_to_show = [f'[{t.get_id()}] {t.get_description()}' for t in user_tasks]

    first_name = user.get_first_name()
    if 0 == len(tasks_to_show):

            update.message.reply_text(message_source[lang]['no_tasks_yet'])
            update.message.reply_text(message_source[lang]['write_me'])


    else:
        keyboard = []
        id = 1
        for task in tasks_to_show:
            keyboard.append([InlineKeyboardButton(str(task), callback_data=str(id))])
            id = id + 1
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(message_source[lang]['your_tasks'].format(first_name),reply_markup=reply_markup)



def select_lang_state(bot, update, context):
    chat = update.message.chat
    user = user_service.create_or_get_user(chat)

    reply_msg = 'Hello'
    if user:
        reply_msg += ', ' + user.get_first_name()
    reply_msg += "\nSelect language:"
    keyboard = [[InlineKeyboardButton("Русский", callback_data='rus'),
                 InlineKeyboardButton("English", callback_data='eng')],
                ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(reply_msg, reply_markup=reply_markup)


def button(bot, update):
    query = update.callback_query
    lang_values = [item.value for item in Language]
    if query.data in lang_values:
        lang = g.automata.set_lang(query.message.chat_id, query.data)
        bot.edit_message_text(text=message_source[lang]['selected_lang'],
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)
        return

    task_id = query.data
    chat = query.message.chat
    user = user_service.create_or_get_user(chat)
    task = task_service.find_task_by_id_and_user_id(task_id, user.get_id())
    # context[CONTEXT_TASK] = task
    task_descr = task.get_description()
    bot.edit_message_text(text=f'[{task_id}]: {task_descr}',
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)


def new_task_state(bot, update, context):
    chat = update.message.chat
    new_task = task_service.create_task(update)
    lang = context[CONTEXT_LANG]
    if new_task:
        context[CONTEXT_TASK] = new_task
        reply_on_success = message_source[lang]['task_created'].format(new_task.get_id())

        user = user_service.create_or_get_user(chat)
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
    if task:
        context[CONTEXT_TASK] = task

        task_descr = task.get_description()

        update.message.reply_text(f'[{task_id}]: {task_descr}')

    else:
        update.message.reply_text(message_source[lang]['cant_find_task'].format(task.get_id()))


def edit_date_state(bot, update, context):
    args = update.message.text.split()
    datetime_args = args[1:]
    latest_task = context[CONTEXT_TASK]

    lang = context[CONTEXT_LANG]
    if latest_task:
        user_id = update.message.chat.id
        latest_task_by_user = task_service.find_task_by_id_and_user_id(latest_task.get_id(), user_id)

        if latest_task_by_user:
            parsed_datetime = handler_utils.parse_date_msg(datetime_args)
            latest_task_by_user.set_next_remind_date(parsed_datetime)
            update.message.reply_text(message_source[lang]['set_date'].format(parsed_datetime))

            update.message.reply_text(f'[{latest_task.get_id()}]: {latest_task.get_description()}')
            return

    update.message.reply_text(f'Sorry, I could not find that task')


def error_state(bot, update, context):
    lastest_task_id = context[CONTEXT_TASK].get_id()
    command_trace = [c.name for c in context[CONTEXT_COMMANDS]]
    lang = context[CONTEXT_LANG]
    update.message.reply_text(message_source[lang]['error'].format(lastest_task_id, command_trace))

