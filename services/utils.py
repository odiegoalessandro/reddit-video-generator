import eyed3
from cleantext import clean
from googletrans import Translator

from constants import *
from services.log import print_error


def translate_text(text):
    translator = Translator()
    translated_text = translator.translate(text, LANGUAGE, "en")
    return translated_text.text


def clean_text(text):
    return clean(text, no_emoji=True, no_punct=True, no_urls=True)


def get_mp3_duration(path):
    try:
        audiofile = eyed3.load(path)
        duration_seconds = audiofile.info.time_secs

        return duration_seconds
    except Exception as e:
        print_error(f"Erro ao obter a duração do arquivo MP3: {str(e)}")

        return 0
