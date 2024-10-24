import sys
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import openai
import pywhatkit as wk
import os
import pyautogui as pi
import time
import numpy as np

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def firstSpeech():
    speak("Hello sir, How can i help you ?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        # check this line
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    firstSpeech()
    while True:
        query = takeCommand().lower()

        if 'open chrome' in query:
            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
            time.sleep(1)
            pi.click(x=1068, y=614, clicks=1, interval=0,button='left')

        elif 'maximise the window' in query:
            pi.hotkey('alt','space')
            time.sleep(1)
            pi.press('x')

        elif 'google search' in query:
            query = query.replace('google search', '')
            pi.hotkey('alt','d')
            pi.write(f"{query}",0.1)
            pi.press('enter')

        elif 'youtube search' in query:
            query = query.replace('youtube search','')
            pi.hotkey('alt','d')
            pi.sleep(1)
            pi.press('tab')
            pi.press('tab')
            pi.press('tab')
            pi.press('tab')
            time.sleep(1)
            pi.write(f"{query}",0.1)
            pi.press('enter')

        elif 'open new window' in query:
            pi.hotkey('ctrl','n')

        elif 'open new tab' in query:
            pi.hotkey('ctrl','t')

        elif 'open incognito window' in query:
            pi.hotkey('ctrl','shift','n')

        elif 'minimise the window' in query:
            pi.hotkey('alt','space')
            time.sleep(1)
            pi.press('n')
        
        elif 'open history' in query:
            pi.hotkey('ctrl','h')

        elif 'open downloads' in query:
            pi.hotkey('ctrl','j')

        elif 'previous tab' in query:
            pi.hotkey('ctrl','shift','tab')

        elif 'next tab' in query:
            pi.hotkey('ctrl','tab')

        elif 'close window' in query:
            pi.hotkey('ctrl','w')

        elif "scroll down" in query:
            scroll_step = 50
            for _ in range(int(800 / scroll_step)):
                pi.scroll(-scroll_step)
                pi.sleep(0.03)

        elif "scroll up" in query:
            scroll_step = 50
            for _ in range(int(800 / scroll_step)):
                pi.scroll(scroll_step)
                pi.sleep(0.03)