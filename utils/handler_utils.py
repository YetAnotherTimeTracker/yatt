"""
Created by anthony on 15.10.17
handler_utils
"""
from time import gmtime, strftime, time

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