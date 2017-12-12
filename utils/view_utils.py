"""
Created by anthony on 07.12.2017
view_utils
"""
import datetime
import os


def render_task_basic(task):
    if task is None:
        raise AssertionError('Task is None')
    return f'[{task.get_id()}]: {task.get_description()}'


def render_task_with_timedelta(task, another_task):
    if task is None:
        raise AssertionError('Task is None')
    if another_task is None:
        raise AssertionError('Task to be checked against is None')

    timedelta = None
    if task.get_next_remind_date() is not None \
            and another_task.get_next_remind_date() is not None:
        timedelta = task.get_next_remind_date() - another_task.get_next_remind_date()

    if timedelta < datetime.timedelta(0):
        timedelta = datetime.timedelta(hours=24) - timedelta

    pretty_print = render_task_basic(task)
    if timedelta:
        hours = timedelta.seconds // 3600
        if 0 != hours:
            pretty_print += f' in {hours} hrs'

        else:
            minutes = timedelta.seconds // 60
            if 0 != minutes:
                pretty_print += f' in {minutes} minutes'

            else:
                pretty_print += f' at the same time'

    return pretty_print


def concat_username(prefix, user, postfix):
    res = ''
    if user and 'none' != user.get_first_name().lower():
        res = prefix + user.get_first_name() + postfix

    else:
        res = prefix + postfix.capitalize()

    return res