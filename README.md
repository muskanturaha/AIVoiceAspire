# AIVoiceAspire

🧠 AI Voice Assistant (with Whisper + GPT + TTS)
This project is a voice assistant that:

Accepts voice input from the user

Transcribes it using OpenAI Whisper

Gets a contextual reply from GPT (via OpenRouter API)

Converts the reply into speech using gTTS

🎯 Features
🌍 Multilingual support (transcribes and replies in the spoken language)

🎤 Click once to start/stop voice recording

🔊 Auto voice playback

🧠 GPT-3.5 reply generation via OpenRouter

🧾 Simple HTML+JS frontend

📁 Project Files
bash
Copy
Edit
.
├── index.html           # Frontend HTML (mic UI + script)
├── style.css            # Frontend styling
├── Pics/                # Icons and background image
├── main.py              # FastAPI server
├── whisper_llm.py       # Whisper + GPT response logic
├── tts.py               # gTTS speech synthesis
├── requirements.txt     # Dependencies
├── telegram_bot.py      # (optional) Telegram integration
├── .env                 # Secrets (OpenRouter, Telegram tokens)
└── reply.mp3            # Generated audio response (temporary)
🚀 Getting Started
🔧 1. Install dependencies
bash
Copy
Edit
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Make sure ffmpeg is installed and available in your system path.

🧪 2. Run the FastAPI Server
bash
Copy
Edit
uvicorn main:app --reload
Runs at: http://127.0.0.1:8000

🌐 3. Use the Web App
Just open index.html in your browser (double-click or drag into Chrome/Edge).
Make sure this line inside <script> points to your backend:

js
Copy
Edit
fetch('http://127.0.0.1:8000/upload', { ...
🔁 If you deploy using ngrok, replace with your HTTPS URL.

🤖 4. (Optional) Use the Telegram Bot
Edit your .env:

ini
Copy
Edit
TELEGRAM_BOT_TOKEN=your_bot_token
OPENROUTER_API_KEY=your_openrouter_key
Then run:

bash
Copy
Edit
python telegram_bot.py
🔑 Environment Variables
Create a .env file in the root directory with:

ini
Copy
Edit
OPENROUTER_API_KEY=your_openrouter_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
📦 Requirements
Install via:

bash
Copy
Edit
pip install -r requirements.txt
Or manually:

txt
Copy
Edit
fastapi
uvicorn
gtts
openai-whisper
torch
python-dotenv
ffmpeg-python
requests
python-telegram-bot==20.7
python-multipart
🖼 Screenshot


🧠 Credits
Whisper

OpenRouter

gTTS

Inspired by natural multimodal human-AI interaction

Let me know if you want a version with GIF/screenshots or a live deployment badge.








Ask ChatGPT
