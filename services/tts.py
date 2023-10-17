from gtts import gTTS

from utils import clean_text, translate_text


def text_to_mp3(filename, text, language):
    if(language != "pt-br"):
        translated_text = translate_text(clean_text(text))
        
        tts = gTTS(text=translated_text, lang="pt-br", slow=False, lang_check=True)
        tts.save(f"{filename}.mp3")
    else:

        tts = gTTS(text=clean_text(text), lang="pt-br", slow=False, lang_check=True)
        tts.save(f"{filename}.mp3")