"""
Created by anthony on 15.10.17
handler_utils
"""
from time import gmtime, strftime, time
import datetime

from config.state_config import CommandType, CommandAliases


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


def parse_date_msg(basedate):

    day = basedate[0]
    month = basedate[1]

    months = ['янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
    month_prefix = month[0: 3]  # декабрь ->дек, дек -> дек
    if month_prefix in months:
        num = str(months.index(month_prefix) + 1)  # 11+1 -> '12'
        if len(num) < 2:
            num = '0' + num
    if month_prefix not in months:
        raise ValueError('Could not recognize provided month')

    if basedate[-1][0: 3] in months:
        time='0.01'
    else:
        time = str(basedate[2]).replace(":", '.').replace("-", '.')

    date_line = str(day) + ' ' + str(num) + ' ' + str(datetime.date.today().year) + ' ' + time

    parse_date = datetime.datetime.strptime(date_line, "%d %m %Y %H.%M")
    return parse_date


def get_command_type(text):
    text = text.strip()
    if not text.startswith('/'):
        return CommandType.ECHO

    else:
        args = text.split()
        for command_type in CommandAliases.keys():
            for alias in CommandAliases.get(command_type):
                if alias == args[0]:
                    return command_type

        raise ValueError('Command not recognized')