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
    """
    Each value defines row(state) in Transition table
    """
    START = 0
    ALL_TASKS = 1
    NEW_TASK = 2
    VIEW_TASK = 3
    EDIT_DATE = 4
    ERROR = 5
    SELECT_LANG = 6


class CommandType(Enum):
    """
    Each value defines column(signal) in Transition table
    """
    UNKNOWN = -1
    START = 0
    ECHO = 1
    VIEW = 2
    DATE = 3
    ALL = 4


class Language(Enum):
    ENG = 'eng'
    RUS = 'rus'


# Defines aliases for each command (signal (column in table))
CommandAliases = {
    CommandType.START: ['/start', '/hi'],
    CommandType.ALL: ['/all'],
    CommandType.VIEW: ['/id', '/task'],
    CommandType.DATE: ['/date'],
    # CommandType.ECHO: ['']
}


class Action(Enum):
    """
    README!
    As short as possible string that is passed with button callback
    since there is a length limit per callback date (only 64 bytes!)
    """
    TASK_MARK_AS_DONE = 'mark_done'
    TASK_DELETE = 'del'
    TASK_DISABLE = 'disable'
    LIST_NOT_DONE = 'not_done'
    LIST_ALL = 'all'
    USER_LANG = 'lang'


# Actions are reduced by action_reducer. But to use them in regular way,
# like we use commands, we need to match each action to appropriate command
# ACTION_TO_COMMAND = {
#     Action.TASK_MARK_AS_DONE: CommandType.VIEW,
#     Action.TASK_DELETE: CommandType.VIEW,
#     Action.TASK_DISABLE: CommandType.VIEW,
#     Action.LIST_NOT_DONE: CommandType.ALL,
#     Action.LIST_ALL: CommandType.ALL,
#     Action.USER_LANG: CommandType.START
# }


# These are keys for fields in callback data passed on button callback
# These strings are also counted as payload in data
# and so should be as short as possible
class CallbackData(Enum):
    """
    ACTION: Actions describe the fact that something happened,
        but don't specify how the application's state changes in response.
        This is the job of reducers.
        (c) React Redux
    DATA: Payload that is used for rendering state
        e.g.: task_id, or flag that should define what to render - all_tasks
        or just completed ones.
    COMMAND: Analogue of regular command that should define which state to render

    In other words:
        COMMAND: which state to render?
        ACTION: how to render?
        DATA: which data to insert into state?
    """
    ACTION = 'act'
    DATA = 'dt'
    COMMAND = 'cmd'
