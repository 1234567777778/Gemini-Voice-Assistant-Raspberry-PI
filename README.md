# Gemini-Voice-Assistant-Raspberry-PI
A Raspberry Pi–based AI voice assistant powered by Google Gemini and Edge Neural TTS. Uses wake-word activation, real-time speech recognition, and natural voice responses. Optimized for low latency, headless operation, and embedded AI projects.

**✨ Features:**

1. Wake word detection (“Jarvis”)
2. Google Gemini AI responses
3. Natural Edge Neural Text-to-Speech
4. ALSA-based audio output
5. Headless terminal operation
6. Optimized for Raspberry Pi

**🧰 Hardware Requirements:**

1. Raspberry Pi 4 / 5 (2 GB RAM minimum, 4 GB recommended)
2. USB microphone (strongly recommended)
3. Speaker / Headphones
4. Internet connection

**🖥️ Software Requirements:**

1. Raspberry Pi OS 64-bit (Bookworm)
2. Python 3.9+
3. ALSA audio system

**⚙️ System Setup (MANDATORY)**

Update your system:
```
sudo apt update && sudo apt upgrade -y
sudo reboot
```
Install audio & build dependencies:
```
sudo apt install mpg123 alsa-utils portaudio19-dev python3-pyaudio -y
```
Add user to audio group:
```
sudo usermod -aG audio $USER
sudo reboot
```

🎤 Audio Device Check

List microphones:
```
arecord -l
```
List speakers:
```
aplay -l
```
Update this line in code if needed:
```
AUDIO_CARD = 3
```

🐍 Python Setup
(Optional but recommended)
```
python3 -m venv venv
source venv/bin/activate
```
Install dependencies:
```
pip install SpeechRecognition edge-tts google-generativeai
```

🔑 Gemini API Setup

1. Get an API key from Google AI Studio
2. Replace in code:
```
API_KEY = "YOUR_GEMINI_API_KEY"
```

▶️ Run the Assistant
```
python3 assistant.py
```

⚠️ Common Fixes

1. No sound → Check AUDIO_CARD
2. Mic not detected → Use USB mic
3. Permission errors → Ensure audio group added
4. High latency → Use Raspberry Pi 4+ and wired internet

📦 Technologies Used

1. Python
2. Google Gemini API
3. Edge Neural TTS
4. SpeechRecognition
5. ALSA / mpg123
6. AsyncIO

📜 License

MIT License – Free to use, modify, and distribute.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-Compatible-red)
![AI](https://img.shields.io/badge/Google-Gemini-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
