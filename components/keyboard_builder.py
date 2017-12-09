"""
Created by anthony on 09.12.2017
keyboard_builder
"""
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


class KeyboardBuilder:
    LABEL = 'button_label'
    DATA = 'button_data'
    # Actions describe the fact that something happened, but don't specify how the app's state changes in response.
    # This is the job of reducers. (c) React Redux
    ACTION = 'button_action'

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
                    new_button = KeyboardBuilder.__create_button(element)
                    button_row.append(new_button)
                buttons.append(button_row)

            # or single button (dict or singleton list of single button)
            elif dict == type(grid_element) or KeyboardBuilder.__is_singleton_list(grid_element):

                new_button = KeyboardBuilder.__create_button(grid_element)
                buttons.append([new_button])

            else:
                raise ValueError('Incorrect type of grid or sub-grid provided')

        kb = InlineKeyboardMarkup(buttons)
        return kb


    @staticmethod
    def __create_button(button_data_map):
        label, data, action = map(button_data_map.get, (KeyboardBuilder.LABEL,
                                                        KeyboardBuilder.DATA,
                                                        KeyboardBuilder.ACTION))
        new_button = InlineKeyboardButton(label, callback_data=data)
        return new_button


    @staticmethod
    def __is_singleton_list(obj):
        return list == type(obj) and 1 == len(obj)
