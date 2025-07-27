from gtts import gTTS

def text_to_speech(text, lang_code="hi"):
    tts = gTTS(text=text, lang=lang_code)
    tts.save("reply.mp3")
    return "reply.mp3"
