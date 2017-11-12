"""
Created by anthony on 12.11.17
state_service
"""
from services import user_service, task_service


def start_state(bot, update):
    chat = update.message.chat
    user = user_service.create_or_get_user(chat)

    reply_msg = 'Hello'
    if user:
        reply_msg += ', ' + user.get_first_name()

    update.message.reply_text(reply_msg)


def all_tasks_state(bot, update):
    chat = update.message.chat
    user = user_service.find_one_by_id(chat.id)
    user_tasks = task_service.find_tasks_by_user_id(user.get_id())

    tasks_to_show = [f'[{t.get_id()}] {t.get_description()}' for t in user_tasks]

    first_name = user.get_first_name()
    if 0 == len(tasks_to_show):
        update.message.reply_text(f'{first_name}, you don\'t have any tasks yet')
        update.message.reply_text('Just write me something to create a new one :)')

    else:
        update.message.reply_text(first_name + ', here are your tasks:\n' + '\n'.join(tasks_to_show))


def new_task_state(bot, update):
    chat = update.message.chat
    new_task = task_service.create_task(update)

    if new_task:
        reply_on_success = f'task with id "{new_task.get_id()}" has been created!'

        user = user_service.find_one_by_id(chat.id)
        if user:
            reply_on_success = user.get_first_name() + ', ' + reply_on_success

        update.message.reply_text(reply_on_success.capitalize())


def view_task_state(bot, update):
    args = update.message.text.split()
    task_id = args[1]

    chat = update.message.chat
    user = user_service.find_one_by_id(chat.id)

    task = task_service.find_task_by_id(task_id, user.get_id())
    if task:
        task_descr = task.get_description()
        update.message.reply_text(f'[{task_id}]: {task_descr}')

    else:
        first_name = user.get_first_name()
        update.message.reply_text(f'Sorry, {first_name}, I couldn\'t find task with id "{task_id}"')


def edit_date_state(bot, update, context):
    args = update.message.text.split()
    datetime = args[1]

    # TODO get task_id from context

    update.message.reply_text(f'Setting date to {datetime}')
