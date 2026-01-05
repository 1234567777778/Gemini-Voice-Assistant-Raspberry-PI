import speech_recognition as sr
from google import genai
import edge_tts
import asyncio
import tempfile
import subprocess
import os
import time
import re

API_KEY = "YOUR_GEMINI_API_KEY" # Replace this with your Gemini API Key
WAKE_WORD = "jarvis"
AUDIO_CARD = 3 # Change this Value to your Speaker Output by running "aplay -l" on your command prompt
AUDIO_DEVICE = f"plughw:{AUDIO_CARD},0"   
VOICE = "en-US-AriaNeural"
LANGUAGE = "en-US"
MAX_WORDS = 50

client = genai.Client(api_key=API_KEY)

recognizer = sr.Recognizer()
recognizer.pause_threshold = 0.8
recognizer.dynamic_energy_threshold = True
mic = sr.Microphone()


def clean_text(text):
    text = re.sub(r"\*", "", text)     
    text = re.sub(r"\s+", " ", text)    
    return text.strip()


async def _speak_async(text):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        audio_path = f.name

    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE
    )

    await communicate.save(audio_path)

    subprocess.run(
        ["mpg123", "-a", AUDIO_DEVICE, audio_path],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    os.remove(audio_path)
    time.sleep(0.2)


def speak(text):
    text = clean_text(text)
    print("Assistant:", text)
    asyncio.run(_speak_async(text))


def listen():
    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio).lower()
    except:
        return ""


print("Gemini Voice Assistant (edge-tts) Running")
print(f"Say '{WAKE_WORD}' to activate\n")

speak("Voice assistant started")

while True:
    text = listen()

    if WAKE_WORD in text:
        print("Wake word detected")
        speak("Yes, how can I help you?")

        command = listen()
        print("You:", command)

        if command in ["exit", "stop", "shutdown", "quit"]:
            speak("Goodbye")
            break

        if command.strip() == "":
            speak("I did not hear anything")
            continue

        try:
            response = client.models.generate_content(
                model="models/gemini-2.5-flash",
                contents=[
                    {
                        "role": "user",
                        "parts": [
                            {
                                "text": (
                                    f"You are a voice assistant. "
                                    f"Answer clearly in at most {MAX_WORDS} words. "
                                    f"Do not use bullet points or special symbols.\n\n"
                                    f"User question: {command}"
                                )
                            }
                        ]
                    }
                ]
            )

            reply = clean_text(response.text)

            print("Gemini:", reply)
            speak(reply)

        except Exception as e:
            print("Error:", e)
            speak("Sorry, something went wrong")

