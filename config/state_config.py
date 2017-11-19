"""
Created by anthony on 12.11.17
automata_config
"""
import collections
from enum import Enum


TRANSITION_TABLE = [
    # start echo    task    date    all
    [1,     0,      0,      0,      0],     # 0. start
    [1,     2,      3,      5,      1],     # 1. all tasks
    [5,     2,      3,      4,      1],     # 2. new task
    [5,     2,      3,      4,      1],     # 3. view task
    [4,     2,      3,      4,      1],     # 4. edit date
    [1,     2,      3,      5,      1]      # 5. error
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
    ALL = 4


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
            self.user_to_context[chat_id] = Context(5)
            return self.user_to_context[chat_id]

    @staticmethod
    def if_can_transit_to(curr_state, command, new_state):
        allowed_state_id = TRANSITION_TABLE[curr_state][command]
        return allowed_state_id == new_state.value

    @staticmethod
    def get_transition(curr_state, command):
        # curr_state and command should instances of classes from above
        new_state_id = TRANSITION_TABLE[curr_state.value][command.value]
        return State(new_state_id)


class Context:
    def __init__(self, history_len):
        self.history_len = history_len
        self.tasks_history = collections.deque(maxlen=history_len)
        self.commands_history = collections.deque(maxlen=history_len)

    def set_task(self, task):
        self.tasks_history.append(task)

    def get_task(self):
        latest_task = None
        if 0 != len(self.tasks_history):
            latest_task = self.tasks_history[len(self.tasks_history) - 1]
        return latest_task

    def set_command(self, command):
        self.commands_history.append(command)

    def get_command(self):
        latest_command = None
        if 0 != len(self.commands_history):
            latest_command = self.commands_history[len(self.commands_history) - 1]
        return latest_command

    def all_tasks(self):
        return self.tasks_history

    def all_commands(self):
        return self.commands_history

    def __repr__(self):
        commands_simplified = [c.name for c in self.commands_history]
        return str(commands_simplified)
