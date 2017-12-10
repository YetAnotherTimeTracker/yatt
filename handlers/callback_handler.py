"""
Created by anthony on 09.12.2017

Actions describe the fact that something happened,
but don't specify how the application's state changes in response.
This is the job of reducers.
(c) React Redux
"""
import json
from telegram.ext import CallbackQueryHandler

import g
from components.automata import CONTEXT_TASK, CONTEXT_LANG
from components.message_source import message_source
from config.state_config import Action, CallbackData, Language
from services import task_service, state_service


def button_handler():
    return CallbackQueryHandler(callback=reduce_action)


def action_handlers():
    return {
        Action.TASK_MARK_AS_DONE: task_mark_as_done,
        Action.TASK_DELETE: task_delete,
        Action.TASK_DISABLE: task_disable,
        Action.LIST_ALL: state_service.all_tasks_state,
        Action.USER_LANG: select_lang
    }


def task_mark_as_done(bot, update, context):
    query = update.callback_query
    chat_id = query.message.chat_id

    task = context[CONTEXT_TASK]
    task.mark_as_completed()
    task_service.update_task(task)

    lang = context[CONTEXT_LANG]
    reply_text = message_source[lang]['btn.view_task.mark_as_done.result']
    bot.send_message(chat_id=chat_id, text=reply_text)


def task_disable(bot, update, context):
    query = update.callback_query
    chat_id = query.message.chat_id

    task = context[CONTEXT_TASK]
    task.mark_as_disabled()
    task_service.update_task(task)

    lang = context[CONTEXT_LANG]
    reply_text = message_source[lang]['btn.view_task.disable_notify.result']
    bot.send_message(chat_id=chat_id, text=reply_text)


def task_delete(bot, update, context):
    query = update.callback_query
    chat_id = query.message.chat_id

    task = context[CONTEXT_TASK]
    task.mark_as_inactive()
    task_service.update_task(task)

    lang = context[CONTEXT_LANG]
    reply_text = message_source[lang]['btn.view_task.delete_task.result']
    bot.send_message(chat_id=chat_id, text=reply_text)


def select_lang(bot, update, context):
    query = update.callback_query
    chat_id = query.message.chat_id

    deserialized = json.loads(query.data)
    # in 'data' field of callback there is 'rus' or 'eng' value
    lang_string = deserialized[CallbackData.DATA.value]

    g.automata.get_context(chat_id)[CONTEXT_LANG] = Language(lang_string)
    lang = context[CONTEXT_LANG]
    reply_text = message_source[lang]['btn.select_lang.' + lang_string + '.result']
    bot.send_message(chat_id=chat_id, text=reply_text)


# context and action
def reduce_action(bot, update):
    query = update.callback_query
    chat_id = query.message.chat_id
    context = g.automata.get_context(chat_id)

    deserialized = json.loads(query.data)
    action = Action(deserialized[CallbackData.ACTION.value])
    data = deserialized[CallbackData.DATA.value]

    handle_function = action_handlers()[action]
    handle_function(bot, update, context)

    print('fuck')
    # query = update.callback_query
    # lang_values = [item.value for item in Language]
    # if query.data in lang_values:
    #     lang = g.automata.get_context(query.message.chat_id)[CONTEXT_LANG] = Language(query.data)
    #     bot.edit_message_text(text=message_source[lang]['selected_lang'],
    #                           chat_id=query.message.chat_id,
    #                           message_id=query.message.message_id)
    #     return
    #
    # task_id = query.data
    # chat = query.message.chat
    # user = user_service.create_or_get_user(chat)
    # task = task_service.find_task_by_id_and_user_id(task_id, user.get_id())
    # # TODO deal with context
    # #context[CONTEXT_TASK] = task
    #
    # if task:
    #     task_descr = task.get_description()
    #     bot.edit_message_text(text=f'[{task_id}]: {task_descr}',
    #                           chat_id=query.message.chat_id,
    #                           message_id=query.message.message_id)
