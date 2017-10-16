"""
Created by anthony on 15.10.17
handler_utils
"""
from time import gmtime, strftime, time


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
