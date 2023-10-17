import os

from gtts import gTTS

from services.utils import clean_text, translate_text


def text_to_mp3(filename, text, language="pt-br"):
    if text:
        final_text = text
        
        if(language != "pt-br"):
            final_text = translate_text(clean_text(text))
            
        if not os.path.exists(os.path.join(os.getcwd(), "voices")):
            os.mkdir(os.path.join(os.getcwd(), "voices"))
        
        tts = gTTS(text=clean_text(final_text), lang="pt-br", slow=False, lang_check=True)
        tts.save(f"{os.path.join(os.getcwd(), "voices")}/{filename}.mp3")
    else:
        print("Parece que esse texto está vazio :(")