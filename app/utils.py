from functools import wraps
from typing import Callable
from config import ChatSettings, TranslationMode
from aiogram import types


def setup_chat_settings(chat_id: int, *, config: dict):
    if chat_id not in config:
        config[chat_id] = ChatSettings()


def chat_settings_registry(config: dict):
    def wrapper(func: Callable):
        @wraps(func)
        async def inner(message: types.Message):
            chat_id = message.chat.id
            setup_chat_settings(chat_id, config=config)
            await func(message)
        return inner
    return wrapper


def switch_mode(settings: ChatSettings):
    match settings.mode:
        case TranslationMode.SELECTIVE:
            settings.mode = TranslationMode.SYNC
        case TranslationMode.SYNC:
            settings.mode = TranslationMode.SELECTIVE
