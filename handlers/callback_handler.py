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
from config.state_config import Action, CallbackData
from services import task_service
from components.keyboard_builder import KeyboardBuilder as kb


def button_handler():
    return CallbackQueryHandler(callback=reduce_action)


def action_handlers():
    return {
        Action.TASK_MARK_AS_DONE: task_mark_as_done,
        Action.TASK_DELETE: task_delete,
        Action.TASK_DISABLE: task_disable
    }


def task_mark_as_done(bot, update, context):
    query = update.callback_query
    chat_id = query.message.chat_id

    task = context[CONTEXT_TASK]
    task.mark_as_completed()
    task_service.update_task(task)

    # lang = context[CONTEXT_LANG]
    # button_grid = kb.view_task_buttons(lang, task.get_id())
    # markup = kb.inline_keyboard(button_grid)

    bot.send_message(chat_id=chat_id, text='Marked as Done')


def task_disable(bot, update, context):
    print('duck')
    return


def task_delete(bot, update, context):
    print('dukc')
    return


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
