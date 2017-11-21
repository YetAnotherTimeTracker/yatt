"""
Created by anthony on 21.11.2017
automata
"""
from components.context import Context
from config.state_config import CommandType, TRANSITION_TABLE, State


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
            self.user_to_context[chat_id] = Context(len(CommandType.__members__))
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
