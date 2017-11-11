"""
Created by anthony on 12.11.17
automata_config
"""

TRANSITION_TABLE = [
#   start   echo    id      date
    [1,     0,      0,      0],     # 0. start
    [1,     2,      3,      5],     # 1. all tasks
    [5,     2,      3,      4],     # 2. new task
    [5,     2,      3,      4],     # 3. view task
    [4,     2,      3,      4],     # 4. edit date
    [1,     2,      3,      5]      # 5. error
]

