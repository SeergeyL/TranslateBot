import os
from enum import Enum

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
MESSAGE_MARKER = os.getenv('MESSAGE_MARKER')
MESSAGE_MARKER_LIST = MESSAGE_MARKER.split(',')
DESTINATION_LANGUAGE = os.getenv('DESTINATION_LANGUAGE')
CONFIDENCE_THRESHOLD = float(os.getenv('CONFIDENCE_THRESHOLD'))


class TranslationMode(Enum):
    SYNC = 'sync'
    SELECTIVE = 'selective'


class ChatSettings(BaseSettings):
    mode: TranslationMode = TranslationMode.SELECTIVE
