"""
Created by anthony on 21.11.2017
filter
"""
from telegram.ext import BaseFilter

from config.state_config import CommandAliases, CommandType


class CustomFilter(BaseFilter):
    def __init__(self):
        super()
        self.supported_commands = self.get_supported_commands()

    '''
    messages required to access bot for the first time (/start) is handled at first 
    all messages that start with '/' should be treated like commands and should have at least one arg
    other messages are passed further (where they create a new task)
    '''
    def filter(self, message):
        text = message.text.strip()
        if text.startswith('/'):
            args = text.split()

            if args[0] in list(CommandAliases[CommandType.START]):
                return True

            return args[0] in self.supported_commands

        else:
            return True


    @staticmethod
    def get_supported_commands():
        handler_lists = list(CommandAliases.values())
        commands = []
        for h_list in handler_lists:
            commands.extend(h_list)

        return commands


command_filter = CustomFilter()
