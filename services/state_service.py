"""
Created by anthony on 12.11.17
state_service
"""
from config.automata_config import TRANSITION_TABLE


class Automata:
    def __init__(self):
        self.user_to_state = {}
        self.user_to_context = {}

    def get_state(self, chat_id_value):
        chat_id = int(chat_id_value)
        if chat_id in self.user_to_state.keys():
            return self.user_to_state[chat_id]

        else:
            self.user_to_state[chat_id] = 0
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