"""
Created by anthony on 09.12.2017
keyboard_builder
"""
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


class KeyboardBuilder:
    LABEL = 'button_label'
    DATA = 'button_data'


    @staticmethod
    def inline_horizontal(button_map):
        """
        Creates _inline_ keyboard with horizontal grid with buttons like this:
        [ English language ][ Русский язык ][ Valyrian language ]
        """
        button_grid = []
        for button in button_map:
            btn_label = button[KeyboardBuilder.LABEL]
            btn_callback_data = button[KeyboardBuilder.DATA]

            new_button = InlineKeyboardButton(btn_label, callback_data=btn_callback_data)
            button_grid.append(new_button)

        kb = InlineKeyboardMarkup([button_grid])
        return kb


    @staticmethod
    def inline_vertical(button_map):
        """
        Creates _inline_ keyboard with horizontal grid with buttons like this:
        [ English language ]
        [ Русский язык ]
        [ Valyrian language ]
        """
        button_grid = []
        # TODO this cycle can be reused in horizontal-button-creation method
        for button in button_map:
            btn_label = button[KeyboardBuilder.LABEL]
            btn_callback_data = button[KeyboardBuilder.DATA]

            new_button = InlineKeyboardButton(btn_label, callback_data=btn_callback_data)
            button_grid.append([new_button])

        kb = InlineKeyboardMarkup(button_grid)
        return kb
