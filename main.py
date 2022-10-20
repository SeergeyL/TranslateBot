import os
from enum import Enum
from aiogram import Bot, Dispatcher, executor, types
from googletrans import Translator

from dotenv import load_dotenv

load_dotenv()


# Environment variables
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
MESSAGE_MARKER = '🇬🇧'


# Initializations
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)
translator = Translator(
    service_urls=[
        'translate.googleapis.com',
    ]
)


class TranslationMode(Enum):
    SELECTIVE = 'selective'
    SYNC = 'sync'


configuration = {
    'mode': TranslationMode.SELECTIVE
}


def translate_message(message: types.Message) -> str:
    translated_message = translator.translate(message.text, dest='en')
    text = f'🤖: {translated_message.text}'
    return text


def check_message_marker(message: str):
    return MESSAGE_MARKER in message


def create_status_message(sep='\n'):
    text = (
        f"Translation mode: *{configuration['mode'].value}*",
    )
    return sep.join(text)


def create_help_message():
    text = (
        '/switch - there are two available translation mods: ' \
            'synchronous translation (*sync*) and selective (*selective*). '\
            f'Selective mode translates messages if they are marked by {MESSAGE_MARKER} in any place in the text. ' \
                'Synchronous translation translates all messages.',
        '/status - show current state of variables',
        '/help - show help message'
    )
    return '\n'.join(text)


@dp.message_handler(commands=['switch'])
async def handle_change_translation_mode(message: types.Message):

    match configuration['mode']:
        case TranslationMode.SELECTIVE:
            configuration['mode'] = TranslationMode.SYNC
        case TranslationMode.SYNC:
            configuration['mode'] = TranslationMode.SELECTIVE

    await message.answer(
        f"Translation mode changed to *{configuration['mode'].value}*",
        parse_mode='Markdown'
    )


@dp.message_handler(commands=['status'])
async def handle_status(message: types.Message):
    await message.answer(create_status_message(), parse_mode='Markdown')


@dp.message_handler(commands=['start', 'help'])
async def handle_menu(message: types.Message):
    status_btn = types.KeyboardButton('/status')
    switch_btn = types.KeyboardButton('/switch')
    description_btn = types.KeyboardButton('/help')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(description_btn)
    keyboard.row(status_btn, switch_btn)

    help_message = create_help_message()
    await message.answer(
        help_message,
        reply_markup=keyboard,
        parse_mode='Markdown'
    )


@dp.message_handler()
async def handle_message(message: types.Message):
    if message.text.startswith('/'):
        await message.answer('Command is not recognized')

    if configuration['mode'] == TranslationMode.SYNC:
        translated = translate_message(message)
        await message.reply(translated)

    elif configuration['mode'] == TranslationMode.SELECTIVE:
        if not check_message_marker(message.text):
            return
        translated = translate_message(message)
        await message.reply(translated)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
