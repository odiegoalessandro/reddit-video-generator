import os

from gtts import gTTS

from services.log import *
from services.utils import clean_text, translate_text


def text_to_mp3(filename, text, language="pt-br"):
    if text:
        final_text = clean_text(text)
        voices_path = os.path.join(os.getcwd(), "voices")

        if (language != "pt-br"):
            final_text = translate_text(final_text)

        if not os.path.exists(voices_path):
            print_warning("Criando diretorio /voices...")
            os.mkdir(voices_path)

        tts = gTTS(text=final_text,
                   lang="pt-br", slow=False, lang_check=True)
        tts.save(f"{voices_path}/{filename}.mp3")
    else:
        print_warning(
            "Aviso! a variavel text está vazia, não foi possivel criar o arquivo .mp3")
