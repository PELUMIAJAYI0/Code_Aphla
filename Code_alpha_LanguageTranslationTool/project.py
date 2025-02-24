import os
import asyncio
from googletrans import Translator
from gtts import gTTS
import pygame

async def translate_text(text, src_lang='auto', dest_lang='en'):
    """
    Translates text asynchronously from one language to another using Google Translate API.
    Converts the translated text into speech using gTTS.
    
    :param text: The text to translate.
    :param src_lang: Source language (default 'auto' for auto-detection).
    :param dest_lang: Target language (default 'en' for English).
    :return: Translated text.
    """
    try:
        translator = Translator()
        translated = await translator.translate(text, src=src_lang, dest=dest_lang)
        translated_text = translated.text

        # Convert text to speech
        tts = gTTS(translated_text, lang=dest_lang)
        audio_file = "translated_audio.mp3"
        tts.save(audio_file)

        # Play the audio file
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

        return translated_text
    except Exception as e:
        return f"Translation Error: {e}"

# Running the async function in a synchronous environment
if __name__ == "__main__":
    text_to_translate = "Hola, ¿cómo estás?"
    
    # Using asyncio to run the async function
    translated_text = asyncio.run(translate_text(text_to_translate, src_lang='es', dest_lang='en'))
    print(f"Translated: {translated_text}")
