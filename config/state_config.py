"""
Created by anthony on 12.11.17
automata_config
"""
from enum import Enum


TRANSITION_TABLE = [
    # start echo    task    date
    [1,     0,      0,      0],     # 0. start
    [1,     2,      3,      5],     # 1. all tasks
    [5,     2,      3,      4],     # 2. new task
    [5,     2,      3,      4],     # 3. view task
    [4,     2,      3,      4],     # 4. edit date
    [1,     2,      3,      5]      # 5. error
]


class State(Enum):
    START = 0
    ALL_TASKS = 1
    NEW_TASK = 2
    VIEW_TASK = 3
    EDIT_DATE = 4
    ERROR = 5


class Command(Enum):
    START = 0
    ECHO = 1
    TASK = 2
    DATE = 3


class Automata:
    def __init__(self):
        self.user_to_state = {}
        self.user_to_context = {}

    def get_state(self, chat_id_value):
        chat_id = int(chat_id_value)
        if chat_id in self.user_to_state.keys():
            return self.user_to_state[chat_id]

        else:
            self.user_to_state[chat_id] = State.START
            return self.user_to_state[chat_id]

    def set_state(self, chat_id, new_state):
        chat_id = int(chat_id)
        self.user_to_state[chat_id] = new_state
        return new_state

    def get_context(self, chat_id_value):
        chat_id = int(chat_id_value)
        if chat_id in self.user_to_context.keys():
            return self.user_to_context[chat_id]

        else:
            self.user_to_context[chat_id] = {}
            return self.user_to_context[chat_id]

    def set_context(self, chat_id, new_context):
        chat_id = int(chat_id)
        self.user_to_context[chat_id] = new_context
        return new_context

    @staticmethod
    def if_can_transit_to(curr_state, command, new_state):
        return new_state == TRANSITION_TABLE[curr_state][command]

    def update_context(self, old_context, new_context):
        pass
