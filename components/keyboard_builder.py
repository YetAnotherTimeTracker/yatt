"""
Created by anthony on 09.12.2017
keyboard_builder
"""
import json
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from components.message_source import message_source
from config.state_config import Action, CallbackData

log = logging.getLogger(__name__)


BTN_LABEL = 'button_label'
BTN_DATA = 'button_data'
# Actions describe the fact that something happened, but don't specify how the app's state changes in response.
# This is the job of reducers. (c) React Redux
BTN_ACTION = 'button_action'

DATA_LIMIT_IN_BYTES = 64


class KeyboardBuilder:
    @staticmethod
    def inline_keyboard(button_grid):
        """
        Creates _inline_ keyboard and returns it's markup with grid of buttons like this:
        [
            { English },
            { Русский }
        ],
        { Exit },
        [
            { X },
            { AB },
            { Y }
        ]

        -->

        [ English ][ Русский ]
        [        Exit        ]
        [  X  ][  AB  ][  Y  ]
        """
        buttons = []
        for grid_element in button_grid:
            # nested element can be a sub-grid (list with buttons)
            if list == type(grid_element) and 1 < len(grid_element):

                button_row = []
                for element in grid_element:
                    new_button = KeyboardBuilder.__create_inline_button(element)
                    button_row.append(new_button)
                buttons.append(button_row)

            # or single button (dict or singleton list of single button)
            elif dict == type(grid_element) or KeyboardBuilder.__is_singleton_list(grid_element):

                new_button = KeyboardBuilder.__create_inline_button(grid_element)
                buttons.append([new_button])

            else:
                raise ValueError('Incorrect type of grid or sub-grid provided')

        kb = InlineKeyboardMarkup(buttons)
        return kb


    @staticmethod
    def __create_inline_button(button_data):
        # this data is passed to callback and is accepted by action reducer
        data = {
            CallbackData.ACTION.value: button_data[BTN_ACTION],
            CallbackData.DATA.value: button_data[BTN_DATA]
        }
        serialized_data = json.dumps(data)

        encoded = serialized_data.encode('utf-8')
        if DATA_LIMIT_IN_BYTES < len(encoded):
            raise ValueError('Too large data is going to be passed to to callback!')

        new_button = InlineKeyboardButton(button_data[BTN_LABEL], callback_data=serialized_data)
        return new_button


    @staticmethod
    def __is_singleton_list(obj):
        return list == type(obj) and 1 == len(obj)


    @staticmethod
    def view_task_buttons(lang, task_id):
        button_map = [
            {
                BTN_LABEL: message_source[lang]['btn.mark_as_done'],
                BTN_DATA: str(task_id),
                BTN_ACTION: Action.TASK_MARK_AS_DONE.value
            },
            [
                {
                    BTN_LABEL: message_source[lang]['btn.disable_notify'],
                    BTN_DATA: str(task_id),
                    BTN_ACTION: Action.TASK_DISABLE.value
                },
                {
                    BTN_LABEL: message_source[lang]['btn.delete_task'],
                    BTN_DATA: str(task_id),
                    BTN_ACTION: Action.TASK_DELETE.value
                }
            ]
        ]
        return button_map
