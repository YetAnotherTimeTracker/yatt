"""
Created by anthony on 15.10.17
handler_utils
"""
from config.state_config import CommandType, CommandAliases


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
