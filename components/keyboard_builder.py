"""
Created by anthony on 09.12.2017
keyboard_builder
"""
import json
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from emoji import emojize

from components.message_source import message_source
from config.state_config import Action, CallbackData, Language, CommandType
from models.project import ProjectType

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
    def btn_task_mark_as_done(lang, task_id):
        return {
            BTN_LABEL: message_source[lang]['btn.view_task.mark_as_done.label'],
            BTN_DATA: str(task_id),
            BTN_ACTION: Action.TASK_MARK_AS_DONE.value,
            BTN_COMMAND: CommandType.VIEW.value
        }


    @staticmethod
    def btn_task_delete(lang, task_id):
        return {
            BTN_LABEL: message_source[lang]['btn.view_task.delete_task.label'],
            BTN_DATA: str(task_id),
            BTN_ACTION: Action.TASK_DELETE.value,
            BTN_COMMAND: CommandType.VIEW.value
        }

    @staticmethod
    def btn_task_disable_notify(lang, task_id):
        return {
            BTN_LABEL: message_source[lang]['btn.view_task.disable_notify.label'],
            BTN_DATA: str(task_id),
            BTN_ACTION: Action.TASK_DISABLE.value,
            BTN_COMMAND: CommandType.VIEW.value
        }

    @staticmethod
    def btn_home(label):
        return {
            BTN_LABEL: label,
            BTN_DATA: 'fuck',  # not used
            BTN_ACTION: Action.START.value,
            BTN_COMMAND: CommandType.START.value
        }

    @staticmethod
    def btn_list_all(label):
        return {
            BTN_LABEL: label,
            BTN_DATA: 'fuck',  # not used
            BTN_ACTION: Action.LIST_ALL.value,
            BTN_COMMAND: CommandType.ALL.value
        }

    @staticmethod
    def btn_list_upcoming(label):
        btn = KeyboardBuilder.btn_list_all(label)
        btn[BTN_ACTION] = Action.LIST_UPCOMING.value
        return btn

    @staticmethod
    def btn_list_completed(label):
        btn = KeyboardBuilder.btn_list_all(label)
        btn[BTN_ACTION] = Action.LIST_COMPLETED.value
        return btn

    @staticmethod
    def view_task_buttons(lang, task_id):
        button_grid = [
            [
                KeyboardBuilder.btn_task_mark_as_done(lang, task_id),
                KeyboardBuilder.btn_task_disable_notify(lang, task_id),
                KeyboardBuilder.btn_task_delete(lang, task_id)
            ],
            [
                KeyboardBuilder.btn_list_upcoming(message_source[lang]['btn.view_task.upcoming.label']),
                KeyboardBuilder.btn_list_all(message_source[lang]['btn.view_task.all.label'])
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
                    BTN_ACTION: Action.SELECTED_LANG.value,
                    BTN_COMMAND: CommandType.LANG.value
                },
                {
                    BTN_LABEL: message_source[lang]['btn.select_lang.rus.label'],
                    BTN_DATA: Language.RUS.value,
                    BTN_ACTION: Action.SELECTED_LANG.value,
                    BTN_COMMAND: CommandType.LANG.value
                }
            ]
        ]
        markup = KeyboardBuilder.create_inline_keyboard(button_grid)
        return markup


    @staticmethod
    def start_state_buttons(lang):
        button_grid = [
            KeyboardBuilder.btn_list_upcoming(message_source[lang]['btn.start_state.to_tasks.upcoming.label']),
            KeyboardBuilder.btn_list_completed(message_source[lang]['btn.start_state.to_tasks.completed.label']),
            KeyboardBuilder.btn_list_all(message_source[lang]['btn.start_state.to_tasks.all.label']),
            {
                BTN_LABEL: message_source[lang]['btn.start_state.select_lang.label'],
                BTN_DATA: 'x7',
                BTN_ACTION: Action.VIEW_LANG.value,
                BTN_COMMAND: CommandType.LANG.value
            }
        ]
        markup = KeyboardBuilder.create_inline_keyboard(button_grid)
        return markup

    @staticmethod
    def select_project_buttons(lang):
        button_grid = [
            [
                {
                    BTN_LABEL: message_source[lang]['btn.new_task.project.personal.label'],
                    BTN_DATA: ProjectType.PERSONAL.value,
                    BTN_ACTION: Action.TASK_PROJECT_SELECTED.value,
                    BTN_COMMAND: CommandType.VIEW.value
                },
                {
                    BTN_LABEL: message_source[lang]['btn.new_task.project.study.label'],
                    BTN_DATA: ProjectType.STUDY.value,
                    BTN_ACTION: Action.TASK_PROJECT_SELECTED.value,
                    BTN_COMMAND: CommandType.VIEW.value
                },
                {
                    BTN_LABEL: message_source[lang]['btn.new_task.project.work.label'],
                    BTN_DATA: ProjectType.WORK.value,
                    BTN_ACTION: Action.TASK_PROJECT_SELECTED.value,
                    BTN_COMMAND: CommandType.VIEW.value
                },
                {
                    BTN_LABEL: message_source[lang]['btn.new_task.project.other.label'],
                    BTN_DATA: ProjectType.OTHER.value,
                    BTN_ACTION: Action.TASK_PROJECT_SELECTED.value,
                    BTN_COMMAND: CommandType.VIEW.value
                }
            ]
        ]
        markup = KeyboardBuilder.create_inline_keyboard(button_grid)
        return markup


    @staticmethod
    def tasks_as_buttons(tasks):
        button_grid = []
        for task in tasks:

            btn_label = task.get_description()
            if task.is_task_completed():
                btn_label = ':white_check_mark: ' + btn_label

            else:
                btn_label = ':black_square_button: ' + btn_label

            task_as_button = [{
                BTN_LABEL: btn_label,
                BTN_DATA: task.get_id(),
                BTN_ACTION: Action.TASK_VIEW.value,
                BTN_COMMAND: CommandType.VIEW.value
            }]
            button_grid.append(task_as_button)
        return button_grid

    @staticmethod
    def all_tasks_buttons(tasks):
        button_grid = KeyboardBuilder.tasks_as_buttons(tasks)
        button_grid.append([
            KeyboardBuilder.btn_list_upcoming('upcoming'),
            KeyboardBuilder.btn_list_completed('completed'),
            KeyboardBuilder.btn_home('home')
        ])
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
                if list == type(grid_element):
                    grid_element = grid_element[0]

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

        new_button = InlineKeyboardButton(emojize(button_data[BTN_LABEL], use_aliases=True),
                                          callback_data=serialized_data)
        return new_button


    @staticmethod
    def __is_singleton_list(obj):
        return list == type(obj) and 1 == len(obj)
