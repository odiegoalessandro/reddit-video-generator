from translate import Translator

from constants import *


def translate_text(text):
    translator = Translator(to_lang=LANGUAGE)

    return translator.translate(text)


def split_text(text):
    segments = []
    current_segment = ""
    text_words = text.split()

    for word in text_words:
        if len(current_segment) + len(word) > LIMIT_OF_CHARS:
            segments.append(current_segment)
            current_segment = word
        else:
            current_segment += (" " if current_segment else "") + word

    if current_segment:
        segments.append(current_segment)

    return segments


def join_text(text_parts):
    complete_text = "".join(text_parts)
    return complete_text
