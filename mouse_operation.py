import pyttsx3
import speech_recognition as sr
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
    speak("Hello sir, what can i do for you ?")

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

        if "close the window" in query:
            pi.click(x=1913, y=21, clicks=1, interval=0,button='left')
        elif "maximise the window" in query:
            pi.click(x=1833, y=18, clicks=1, interval=0,button='left')
        elif "minimise the window" in query:
            pi.click(x=1780, y=13, clicks=1, interval=0,button='left')

        elif "like this video" in query:
            print("Everyone who are watching this video, please give a thumbs up to this")
            speak("Everyone who are watching this video, please give a thumbs up to this")
            pi.press('win')
            time.sleep(1.5)
            speak('open the browser')
            pi.typewrite('chrome',0.1)
            time.sleep(1)
            pi.press('enter')
            time.sleep(1)
            speak('select your account')
            time.sleep(1)
            pi.click(x=1068, y=614, clicks=1, interval=0,button='left')
            time.sleep(1)
            speak("type linkedin.com")
            pi.write('https://www.linkedin.com/feed/',0.1)
            time.sleep(1)
            speak('enter')
            pi.press('enter')
            speak('Now search for this video and please give a thumbs up to this...')

        # elif "open gemini" in query:
        #     print("Opening gemini chatbot...")
        #     speak("Opening gemini chatbot...")
        #     pi.press('win')
        #     time.sleep(1)
        #     pi.typewrite('chrome',0.1)
        #     time.sleep(1)
        #     pi.press('enter')
        #     time.sleep(1)
        #     pi.click(x=1068, y=614, clicks=1, interval=0,button='left')
        #     time.sleep(1)
        #     pi.click(x=684, y=786, clicks=1, interval=0,button='left')
        #     time.sleep(1)
        #     pi.press('enter')

        # elif "open github" in query:
        #     print("Opening your github...")
        #     pi.press('win')
        #     time.sleep(1)
        #     pi.typewrite('chrome',0.1)
        #     time.sleep(1)
        #     pi.press('enter')
        #     time.sleep(1)
        #     pi.click(x=1068, y=614, clicks=1, interval=0,button='left')
        #     time.sleep(1)
        #     pi.click(x=963, y=787, clicks=1, interval=0,button='left')
        #     time.sleep(1)
        #     pi.press('enter')
        #     time.sleep(1)
        #     speak("here's your github account sir...")

        # elif "open whatsapp" in query:
        #     print("Opening your whatsapp...")
        #     pi.press('win')
        #     time.sleep(1)
        #     pi.typewrite('chrome',0.1)
        #     time.sleep(1)
        #     pi.press('enter')
        #     time.sleep(1)
        #     pi.click(x=1068, y=614, clicks=1, interval=0,button='left')
        #     time.sleep(1)
        #     pi.click(x=815, y=656, clicks=1, interval=0,button='left')
        #     time.sleep(1)
        #     pi.press('enter')
        #     time.sleep(1)
        #     speak("here's your whatsapp sir...")

        elif "new tab" in query:
            pi.keyDown('ctrl')
            pi.press('t')
            pi.keyUp('ctrl')

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

        elif 'open gemini' in query:
            img = pi.locateCenterOnScreen('1.png')
            pi.doubleClick(img)
            # pi.hotkey('alt','space')
            # time.sleep(1)
            # pi.press('x')
            time.sleep(2)
            pi.click(x=1068, y=614, clicks=1, interval=0,button='left')

            image_path = os.path.join(os.getcwd(), "screenshot10.png")
            
            try:
                time.sleep(1.5)
                pi.press('esc')
                img2 = pi.locateCenterOnScreen(image_path)
                pi.click(img2)
            except pi.ImageNotFoundException:
                print("Gemini icon not found on screen.")

        elif 'open whatsapp' in query:
            img = pi.locateCenterOnScreen('1.png')
            pi.doubleClick(img)
            # pi.hotkey('alt','space')
            # time.sleep(1)
            # pi.press('x')
            time.sleep(1)
            pi.click(x=1068, y=614, clicks=1, interval=0,button='left')

            image_path = os.path.join(os.getcwd(), "whatsapp.png")
            
            try:
                time.sleep(1)
                pi.press('esc')
                img2 = pi.locateCenterOnScreen(image_path)
                pi.click(img2)
            except pi.ImageNotFoundException:
                print("whatsapp icon not found on screen.")


        elif 'open github' in query:
            img = pi.locateCenterOnScreen('1.png')
            pi.doubleClick(img)
            # pi.hotkey('alt','space')
            # time.sleep(1)
            # pi.press('x')
            time.sleep(1)
            pi.click(x=1068, y=614, clicks=1, interval=0,button='left')

            image_path = os.path.join(os.getcwd(), "github.png")
            
            try:
                time.sleep(1)
                pi.press('esc')
                img2 = pi.locateCenterOnScreen(image_path)
                pi.click(img2)
                speak("here's your github sir...")
            except pi.ImageNotFoundException:
                print("github icon not found on screen.")


        # elif 'select person one' or 'select person 1' in query:
        #     time.sleep(1)
        #     pi.press('esc')
        #     img1 = pi.locateCenterOnScreen('5.png')
        #     pi.click(img1)
        #     time.sleep(1)
        #     pi.press('esc')
        #     img2 = pi.locateCenterOnScreen('7.png')
        #     pi.click(img2)

        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")
            