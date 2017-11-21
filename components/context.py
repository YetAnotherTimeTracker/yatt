"""
Created by anthony on 21.11.2017
context
"""
import collections


class Context:
    def __init__(self, history_len):
        self.history_len = history_len
        self.tasks_history = []
        self.commands_history = collections.deque(maxlen=history_len)

    def add_task(self, task):
        self.tasks_history.append(task)
        print('fuck')

    def get_task(self):
        latest_task = None
        if 0 != len(self.tasks_history):
            latest_task = self.tasks_history[len(self.tasks_history) - 1]
        return latest_task

    def add_command(self, command):
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
        tasks_simplified = []
        i = 0
        while i < len(self.tasks_history):
            tasks_simplified.append(self.tasks_history.__getitem__(i))
        commands_simplified = [c.name for c in self.commands_history]
        return f'commands: {str(commands_simplified)}\ntasks: {str(tasks_simplified)}'
