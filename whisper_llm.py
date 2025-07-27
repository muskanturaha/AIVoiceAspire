import whisper
import requests
import os
from dotenv import load_dotenv

load_dotenv()
model = whisper.load_model("medium")

def transcribe_audio(path):
    result = model.transcribe(path, task="transcribe")
    transcript = result["text"]
    detected_lang = result["language"]  # e.g., 'hi', 'bn', 'ta'
    return transcript, detected_lang

def get_reply_from_llm(text, lang):
    api_key = os.getenv("OPENROUTER_API_KEY")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    prompt = f"""
You are a helpful assistant for Indian welfare schemes.
Reply in {lang} script (Hindi = देवनागरी, Bengali = বাংলা, Tamil = தமிழ்).
Always be friendly and conversational. Ask follow-up if needed.
"""

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": text}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"]
