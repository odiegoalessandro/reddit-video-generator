from cleantext import clean
from googletrans import Translator

from constants import *


def translate_text(text):
    translator = Translator()
    translated_text = translator.translate(text, LANGUAGE, "en")
    return translated_text.text


def clean_text(text):
    return clean(text, no_emoji=True, no_punct=True, no_urls=True)
