"""
Created by anthony on 12.11.17
automata_config
"""
from enum import Enum


TRANSITION_TABLE = [
    # start echo    task    date    all
    [1,     0,      0,      0,      0],     # 0. start
    [1,     2,      3,      5,      1],     # 1. all tasks
    [1,     2,      3,      4,      1],     # 2. new task
    [1,     2,      3,      4,      1],     # 3. view task
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


class CommandType(Enum):
    UNKNOWN = -1
    START = 0
    ECHO = 1
    TASK = 2
    DATE = 3
    ALL = 4


CommandAliases = {
    CommandType.START: ['/start', '/hi'],
    CommandType.ALL: ['/all'],
    CommandType.TASK: ['/id', '/task'],
    CommandType.DATE: ['/date'],
    # CommandType.ECHO: ['']
}
