"""
Created by anthony on 07.12.2017
date_utils
"""
from datetime import datetime, timedelta
from random import randrange
from time import strftime, gmtime, time


def random_date(start, end):
    """
    This function will return a random datetime between two datetime objects.
    https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


# TODO fix to support 3 inputs: date-month-time, date-time, time
def parse_date_msg(basedate):

    day = basedate[0]
    month = basedate[1]

    months = ['янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
    month_eng = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    month_prefix = month[0: 3]  # декабрь ->дек, дек -> дек
    if (month_prefix in months) or (month_prefix in month_eng):
        num = None
        if month_prefix in months:
            num = str(months.index(month_prefix) + 1)

        else:
            num = str(month_eng.index(month_prefix) + 1)

        if len(num) < 2:
            num = '0' + num
    if month_prefix not in months:
        raise ValueError('Could not recognize provided month')

    if basedate[-1][0: 3] in months:
        time = '0.01'
    else:
        time = str(basedate[2]).replace(":", '.').replace("-", '.')

    date_line = str(day) + ' ' + str(num) + ' ' + str(datetime.date.today().year) + ' ' + time

    parse_date = datetime.strptime(date_line, "%d %m %Y %H.%M")
    return parse_date


def current_time():
    return strftime("%H:%M %d-%m-%Y", gmtime())


# decorator from lecture
def add_timestamp(func):
    def inner_func(text_arg):
        ret = func(f'{text_arg} ...sent on {current_time()}')
        return ret

    return inner_func


def log_duration(func):
    def inner_func(*args):
        start_time = time()
        ret = func(args)

        print(f'execution time: {time() - start_time} seconds')
        return ret

    return inner_func


def seconds_between_tasks(task1, task2):
    return (task1.get_next_remind_date() - task2.get_next_remind_date()).total_seconds()


def readable_datetime(datetime_to_parse):
    if datetime_to_parse is None:
        return '-'

    else:
        return datetime.strftime(datetime_to_parse, "%d %b %H:%M")
