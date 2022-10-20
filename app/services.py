from googletrans import Translator

import config
from labels import RESPONSE_TEXT


class TranslationService:
    def __init__(self, service_urls, **kwargs):
        self.translator = Translator(service_urls=service_urls, **kwargs)

    def check_language(self, message: str) -> bool:
        lang = self.translator.detect(message)
        is_destination_lang = lang.lang == config.DESTINATION_LANGUAGE
        lang_confidence = lang.confidence > config.CONFIDENCE_THRESHOLD
        if  is_destination_lang and lang_confidence:
            return True
        return False

    def translate(
        self,
        text: str,
        mode: config.TranslationMode,
    ) -> None | str:
        if self.check_language(text):
            return None

        if mode == config.TranslationMode.SYNC:
            translated = self.translator.translate(
                text,
                dest=config.DESTINATION_LANGUAGE
            )
            return RESPONSE_TEXT['translated'].format(text=translated.text)

        if config.MESSAGE_MARKER not in text:
            return None

        translated = self.translator.translate(
            text,
            dest=config.DESTINATION_LANGUAGE
        )
        return RESPONSE_TEXT['translated'].format(text=translated.text)
