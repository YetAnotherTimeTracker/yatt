"""
Created by anthony on 21.11.2017
filter
"""
import logging

from config.state_config import CommandAliases, CommandType


class CustomFilter:
    def __init__(self):
        self.supported_commands = self.get_supported_commands()

    '''
    message required to access bot for the first time (/start) is handled at first 
    all messages that start with '/' should be treated as commands and should have at least one arg
    other messages (echo) are passed further
    '''
    def known_command(self, text):
        logging.debug(f'filtering message {text}')
        text = text.strip()
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
