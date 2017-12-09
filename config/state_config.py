"""
Created by anthony on 12.11.17
automata_config
"""
from enum import Enum


TRANSITION_TABLE = [
    # start echo    task    date    all
    [6,     0,      0,      0,      0],     # 0. start
    [6,     2,      3,      5,      1],     # 1. all tasks
    [1,     2,      3,      4,      1],     # 2. new task
    [3,     2,      3,      4,      1],     # 3. view task
    [4,     2,      3,      4,      1],     # 4. edit date
    [6,     2,      3,      5,      1],     # 5. error
    [6,     1,      5,      5,      1]      # 6. select language
]


class State(Enum):
    START = 0
    ALL_TASKS = 1
    NEW_TASK = 2
    VIEW_TASK = 3
    EDIT_DATE = 4
    ERROR = 5
    SELECT_LANG = 6


class CommandType(Enum):
    UNKNOWN = -1
    START = 0
    ECHO = 1
    TASK = 2
    DATE = 3
    ALL = 4


class Language(Enum):
    ENG = 'eng'
    RUS = 'rus'


CommandAliases = {
    CommandType.START: ['/start', '/hi'],
    CommandType.ALL: ['/all'],
    CommandType.TASK: ['/id', '/task'],
    CommandType.DATE: ['/date'],
    # CommandType.ECHO: ['']
}


class Action(Enum):
    # string here should be as short as possible
    # since there is a length limit per callback data
    TASK_MARK_AS_DONE = 'mark_done'
    TASK_DELETE = 'del'
    TASK_DISABLE = 'disable'


class CallbackData(Enum):
    DATA = 'callback_data'
    ACTION = 'callback_action'
