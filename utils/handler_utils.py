"""
Created by anthony on 15.10.17
handler_utils
"""
import json

from config.state_config import CommandType, CommandAliases, Action, CallbackData


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


def deserialize_data(data):
    """
    deserialize callback data into Action, CommandType, data
    """
    deserialized = json.loads(data)
    action = Action(deserialized[CallbackData.ACTION.value])
    command = CommandType(deserialized[CallbackData.COMMAND.value])
    data = deserialized[CallbackData.DATA.value]
    return {
        CallbackData.ACTION: action,
        CallbackData.COMMAND: command,
        CallbackData.DATA: data
    }


def is_callback(update):
    return update.callback_query is not None
