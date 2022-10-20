from aiogram import types
from labels import BUTTON_LABELS

def base_keyboard():
    status_btn = types.KeyboardButton(BUTTON_LABELS['status'])
    switch_btn = types.KeyboardButton(BUTTON_LABELS['switch'])
    description_btn = types.KeyboardButton(BUTTON_LABELS['help'])
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(description_btn)
    keyboard.row(status_btn, switch_btn)
    return keyboard
