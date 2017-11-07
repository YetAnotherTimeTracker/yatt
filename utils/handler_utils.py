"""
Created by anthony on 15.10.17
handler_utils
"""
from time import gmtime, strftime, time
import datetime

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

def date(args):
    
    day = args[0]
    month = args[1]

    months = ['янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
    month_prefix = month[0: 3]  # декабрь ->дек, дек -> дек
    if month_prefix in months:
        num = str(months.index(month_prefix) + 1)  # 11+1 -> '12'
        if len(num) < 2:
            num = '0' + num

    time = str(args[2]).replace(":", '.').replace("-", '.')
    date_line = str(day) + ' ' + str(num) + ' ' + str(datetime.date.today().year) + ' ' + time

    d = datetime.datetime.strptime(date_line, "%d %m %Y %H.%M")
    return d
