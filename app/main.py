from aiogram import Bot, Dispatcher, executor, types

import config
from keyboards import base_keyboard
from labels import RESPONSE_TEXT
from services import TranslationService
from utils import chat_settings_registry, switch_mode

bot = Bot(token=config.TELEGRAM_TOKEN)
dp = Dispatcher(bot)
translator = TranslationService(['translate.googleapis.com'])

# In memory chat settings
CHAT_SETTINGS = {}


@dp.message_handler(commands=['start', 'help'])
@chat_settings_registry(CHAT_SETTINGS)
async def handle_start(message: types.Message):
    keyboard = base_keyboard()
    await message.answer(
        RESPONSE_TEXT['help'].format(config.MESSAGE_MARKER),
        reply_markup=keyboard,
        parse_mode='Markdown'
    )


@dp.message_handler(commands=['status'])
@chat_settings_registry(CHAT_SETTINGS)
async def handle_status(message: types.Message):
    chat_id = message.chat.id
    settings = CHAT_SETTINGS[chat_id]
    response = RESPONSE_TEXT['status'].format(mode=settings.mode.value)
    await message.answer(response, parse_mode='Markdown')


@dp.message_handler(commands=['switch'])
@chat_settings_registry(CHAT_SETTINGS)
async def handle_switch(message: types.Message):
    settings = CHAT_SETTINGS[message.chat.id]
    switch_mode(settings)
    await message.answer(
        RESPONSE_TEXT['switch'].format(mode=settings.mode.value),
        parse_mode='Markdown'
    )


@dp.message_handler()
@chat_settings_registry(CHAT_SETTINGS)
async def handle_message(message: types.Message):
    if message.text.startswith('/'):
        return

    settings = CHAT_SETTINGS[message.chat.id]
    translated = translator.translate(message.text, settings.mode)
    if translated:
        await message.reply(translated)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
