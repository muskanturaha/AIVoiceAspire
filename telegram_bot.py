import os
import subprocess
import asyncio
from telegram import Update, InputFile
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters,
)
from whisper_llm import transcribe_audio, get_reply_from_llm
from tts import text_to_speech
from dotenv import load_dotenv

# 🔐 Load API keys
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# 🧠 Make sure 'audios' directory exists
os.makedirs("audios", exist_ok=True)

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    file = await update.message.voice.get_file()
    ogg_path = f"audios/{user_id}_{file.file_id}.ogg"
    await file.download_to_drive(ogg_path)

    await update.message.reply_text("🎙️ Audio received. Transcribing...")

    # 🔄 Convert to .wav
    wav_path = ogg_path.replace(".ogg", ".wav")
    subprocess.run(["ffmpeg", "-y", "-i", ogg_path, wav_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # ✨ Transcribe + detect language
    transcript, lang_code = transcribe_audio(wav_path)

    # 🧠 LLM reply
    reply = get_reply_from_llm(transcript, lang_code)

    # 🔊 Voice reply
    mp3_path = text_to_speech(reply, lang_code)

    # 💬 Send text + audio reply
    await update.message.reply_text(f"📝 You said:\n{transcript}")
    await update.message.reply_text(f"🤖 {reply}")
    await update.message.reply_voice(voice=InputFile(mp3_path))

async def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))
    await app.run_polling()
