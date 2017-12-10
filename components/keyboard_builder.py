"""
Created by anthony on 09.12.2017
keyboard_builder
"""
import json
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from components.message_source import message_source
from config.state_config import Action, CallbackData, Language, CommandType

log = logging.getLogger(__name__)


BTN_LABEL = 'button_label'
BTN_DATA = 'button_data'
BTN_COMMAND = 'button_command_analogue'
# Actions describe the fact that something happened, but don't specify how the app's state changes in response.
# This is the job of reducers. (c) React Redux
BTN_ACTION = 'button_action'

DATA_LIMIT_IN_BYTES = 64


class KeyboardBuilder:

    @staticmethod
    def view_task_buttons(lang, task_id):
        button_grid = [
            {
                BTN_LABEL: message_source[lang]['btn.view_task.mark_as_done.label'],
                BTN_DATA: str(task_id),
                BTN_ACTION: Action.TASK_MARK_AS_DONE.value,
                BTN_COMMAND: CommandType.VIEW.value
            },
            [
                {
                    BTN_LABEL: message_source[lang]['btn.view_task.disable_notify.label'],
                    BTN_DATA: str(task_id),
                    BTN_ACTION: Action.TASK_DISABLE.value,
                    BTN_COMMAND: CommandType.VIEW.value
                },
                {
                    BTN_LABEL: message_source[lang]['btn.view_task.delete_task.label'],
                    BTN_DATA: str(task_id),
                    BTN_ACTION: Action.TASK_DELETE.value,
                    BTN_COMMAND: CommandType.VIEW.value
                }
            ],
            [
                {
                    BTN_LABEL: message_source[lang]['btn.view_task.not_completed.label'],
                    BTN_DATA: 'not_completed',
                    BTN_ACTION: Action.LIST_NOT_DONE.value,
                    BTN_COMMAND: CommandType.ALL.value
                },
                {
                    BTN_LABEL: message_source[lang]['btn.view_task.all_tasks.label'],
                    BTN_DATA: 'all_tasks',
                    BTN_ACTION: Action.LIST_ALL.value,
                    BTN_COMMAND: CommandType.ALL.value
                }
            ]
        ]
        markup = KeyboardBuilder.create_inline_keyboard(button_grid)
        return markup

    @staticmethod
    def select_lang_buttons(lang):
        button_grid = [
            [
                {
                    BTN_LABEL: message_source[lang]['btn.select_lang.eng.label'],
                    BTN_DATA: Language.ENG.value,
                    BTN_ACTION: Action.USER_LANG.value,
                    BTN_COMMAND: CommandType.START.value
                },
                {
                    BTN_LABEL: message_source[lang]['btn.select_lang.rus.label'],
                    BTN_DATA: Language.RUS.value,
                    BTN_ACTION: Action.USER_LANG.value,
                    BTN_COMMAND: CommandType.START.value
                }
            ]
        ]
        markup = KeyboardBuilder.create_inline_keyboard(button_grid)
        return markup


    @staticmethod
    def create_inline_keyboard(button_grid):
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
            CallbackData.DATA.value: button_data[BTN_DATA],
            CallbackData.COMMAND.value: button_data[BTN_COMMAND]
        }
        serialized_data = json.dumps(data)

        encoded = serialized_data.encode('utf-8')
        if len(encoded) > DATA_LIMIT_IN_BYTES:
            raise ValueError(f'Too large data is going to be passed to to callback: '
                             f'{len(encoded)} bytes. Limit: {DATA_LIMIT_IN_BYTES} bytes')

        new_button = InlineKeyboardButton(button_data[BTN_LABEL], callback_data=serialized_data)
        return new_button


    @staticmethod
    def __is_singleton_list(obj):
        return list == type(obj) and 1 == len(obj)
