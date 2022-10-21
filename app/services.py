from googletrans import Translator

import config
from labels import RESPONSE_TEXT


class TranslationService:
    def __init__(self, service_urls, **kwargs):
        self.translator = Translator(service_urls=service_urls, **kwargs)

    def should_translate(self, message: str) -> bool:
        lang = self.translator.detect(message)
        is_destination_lang = lang.lang == config.DESTINATION_LANGUAGE
        lang_confidence = lang.confidence > config.CONFIDENCE_THRESHOLD
        if is_destination_lang and lang_confidence:
            return False
        return True

    def check_message_marker(self, text):
        return any([marker in text for marker in config.MESSAGE_MARKER_LIST])

    def translate(
        self,
        text: str,
        mode: config.TranslationMode,
    ) -> None | str:
        if not self.should_translate(text):
            return None

        if mode == config.TranslationMode.SYNC:
            translated = self.translator.translate(
                text,
                dest=config.DESTINATION_LANGUAGE
            )
            return RESPONSE_TEXT['translated'].format(text=translated.text)

        if not self.check_message_marker(text):
            return None

        translated = self.translator.translate(
            text,
            dest=config.DESTINATION_LANGUAGE
        )
        return RESPONSE_TEXT['translated'].format(text=translated.text)
