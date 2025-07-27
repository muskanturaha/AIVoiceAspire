from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from whisper_llm import transcribe_audio, get_reply_from_llm
from tts import text_to_speech
import os
from pydub import AudioSegment

app = FastAPI()

@app.post("/process")
async def process_audio(file: UploadFile = File(...)):
    audio_path = "input_audio.wav"
    with open(audio_path, "wb") as f:
        f.write(await file.read())

    # Convert to WAV mono/16kHz
    sound = AudioSegment.from_file(audio_path)
    sound = sound.set_channels(1).set_frame_rate(16000)
    sound.export(audio_path, format="wav")

    # Transcribe & detect language
    transcript, detected_lang = transcribe_audio(audio_path)

    # Get LLM reply
    reply = get_reply_from_llm(transcript, detected_lang)

    # Generate voice reply
    audio_reply = text_to_speech(reply, lang_code=detected_lang)

    return JSONResponse({
        "transcript": transcript,
        "language": detected_lang,
        "reply": reply,
        "audio_url": "/speak"
    })

@app.get("/speak")
def speak():
    return FileResponse("reply.mp3", media_type="audio/mpeg")

