import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

# -----------------------------
# CONFIG
# -----------------------------
NEWS_API_KEY = "<YOUR_NEWS_API_KEY>"
OPENAI_KEY = "<YOUR_OPENAI_API_KEY>"

# -----------------------------
# SPEECH FUNCTIONS
# -----------------------------
def speak(text):
    """Convert text to speech using gTTS + pygame"""
    tts = gTTS(text)
    tts.save('temp.mp3')

    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")

# -----------------------------
# AI PROCESSING
# -----------------------------
def aiProcess(command):
    client = OpenAI(api_key=OPENAI_KEY)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis. Give short answers."},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

# -----------------------------
# COMMAND HANDLER
# -----------------------------
def processCommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")

    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")

    elif c.startswith("play "):
        song = c.split(" ", 1)[1].lower()
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find {song} in your music library.")

    elif "news" in c:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get("articles", [])
                for article in articles[:5]:  # read only top 5 headlines
                    speak(article['title'])
            else:
                speak("Sorry, I couldn't fetch the news right now.")
        except Exception as e:
            speak("Error fetching news.")

    else:
        # fallback to OpenAI
        output = aiProcess(c)
        speak(output)

# -----------------------------
# MAIN LOOP
# -----------------------------
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
                word = recognizer.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yes?")
                print("Wake word detected. Listening for command...")

                with sr.Microphone() as source:
                    audio = recognizer.listen(source, timeout=5)
                    command = recognizer.recognize_google(audio)

                print(f"Command received: {command}")
                processCommand(command)

        except sr.WaitTimeoutError:
            continue
        except sr.UnknownValueError:
            continue
        except Exception as e:
            print(f"Error: {e}")
