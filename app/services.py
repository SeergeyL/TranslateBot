from googletrans import Translator
from config import TranslationMode, DESTINATION_LANGUAGE, MESSAGE_MARKER
from labels import RESPONSE_TEXT


class TranslationService:
    def __init__(self, service_urls, **kwargs):
        self.translator = Translator(service_urls=service_urls, **kwargs)

    def translate(
        self,
        text: str,
        mode: TranslationMode,
    ) -> None | str:
        if mode == TranslationMode.SYNC:
            translated = self.translator.translate(
                text,
                dest=DESTINATION_LANGUAGE
            )
            return RESPONSE_TEXT['translated'].format(text=translated.text)

        if MESSAGE_MARKER not in text:
            return None

        translated = self.translator.translate(
            text,
            dest=DESTINATION_LANGUAGE
        )
        return RESPONSE_TEXT['translated'].format(text=translated.text)
