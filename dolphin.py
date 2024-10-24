import sys
import pyttsx3 
import datetime
import speech_recognition as sr 
import wikipedia 
import webbrowser
import openai 
import pywhatkit as wk
import os
import pyautogui
import time
import numpy as np
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
volRange = volume.GetVolumeRange()

minVol = volRange[0]
maxVol = volRange[1]

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def ask_chatgpt(question):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        engine="text-embedding-ada-002",  
        prompt=question,
        max_tokens=100, 
        n=1,  
        stop=None  
    )

    # Extract the first generated response and strip extra characters
    return response.choices[0].text.strip()

def set_volume_to_percent(desired_percent):
    """Setting the system volume to the specified percentage."""
    speak(f"Setting volume to {desired_percent}")
    desired_volume = np.interp(desired_percent, [0, 100], [minVol, maxVol])
    volume.SetMasterVolumeLevel(desired_volume, None)

def wishme():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 0 and hour <12):
        speak("Good morning!")
    elif( hour >=12 and hour <18):
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    
    speak("I'm Ready to Comply, What can i do for you ?")

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
    wishme()
    while True:
        query = takeCommand().lower()
        if 'dolphin' in query:
            print("yes sir")
            speak("yes sir")

        elif "who are you" in query:
            print("My name is Dolphin, and I'm at your service! I'm a Jarvis program built using Python, designed to assist you with various tasks.  I can recognize images on your screen, click on them to automate actions, and even handle over 85 common PC tasks you perform daily.  Just tell me what you need, and I'll do my best to help!")
            speak("My name is Dolphin, and I'm at your service! I'm a Jarvis program built using Python, designed to assist you with various tasks.  I can recognize images on your screen, click on them to automate actions, and even handle over 85 common PC tasks you perform daily.  Just tell me what you need, and I'll do my best to help!")
            # print("I can do Everthing my creator programmed me to do")
            # speak("I can do Everthing my creator programmed me to do")

        elif "who created you" in query:
            print("His name is Suraj Patra, I'm created with Python programming language, in Visual Studio Code.")
            speak("His name is Suraj Patra, I'm created with Python programming language, in Visual Studio Code.")

        elif "what is" in query:
            speak("Searching Wikipedia...")
            query = query.replace("what is","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "who is" in query:
            speak("Searching Wikipedia...")
            query = query.replace("who is","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "tell me about" in query:
            speak("Searching Wikipedia...")
            query = query.replace("Tell me about","")
            # results = ask_chatgpt(query)
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "just open google" in query:
            webbrowser.open('google.com')
        
        elif "open google" in query:
            speak("What do you want to know ?")
            qry = takeCommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=2)
            speak(results)

        elif "open whatsapp" in query:
            webbrowser.open('https://web.whatsapp.com/')

        elif "just open youtube" in query:
            webbrowser.open('youtube.com')

        elif "open youtube" in query:
            speak("what you will like to watch ?")
            query = takeCommand().lower()
            wk.playonyt(f"{query}")

        elif "search on youtube" in query:
            query = query.replace("search on youtube","")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")

        elif "play" in query:
            speak("here's your song sir...")
            query = query.replace("play","")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")
            wk.playonyt(f"www.youtube.com/results?search_query={query}")

        elif "close microsoft edge" in query:
            os.system("taskkill /f /im msedge.exe")

        elif "close chrome" in query:
            os.system("taskkill /f /im chrome.exe")


        # ******************* MORE SPECIFIC TASKS ***********************
        # elif "open cmd" or "open command prompt" in query:
        #     os.system("start cmd")

        # elif "close cmd" or "close command prompt" in query:
        #     os.system("taskkill /f /im cmd.exe")

        elif "open word" in query:
            npath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(npath)

        elif "close word" in query:
            os.system("taskkill /f /im msword.exe")

        elif "open gallery" in query:
            gallerypath = "C:\\Local Disk D\\Camera"
            os.startfile(gallerypath)

        elif "what is the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "hibernate the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "take screenshot" in query:
            speak('tell me a name for the file')
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot saved")

        elif "go to sleep" in query:
            speak('alright then, I am switching off')
            sys.exit()
        
        elif "set volume to" in query:
            desired_percent = int(query.replace("set volume to ", ""))
            set_volume_to_percent(desired_percent)

        elif "close the window" in query:
            speak('closing the window...')
            pyautogui.click(x=1913, y=21, clicks=1, interval=0,button='left')

        elif "maximise the window" in query:
            pyautogui.click(x=1833, y=18, clicks=1, interval=0,button='left')
        elif "minimise the window" in query:
            pyautogui.click(x=1780, y=13, clicks=1, interval=0,button='left')

        # elif "mute" or "unmute" in query:
        #     pyautogui.press("volumemute")