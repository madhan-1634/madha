import pyttsx3
import pywhatkit as kit
import datetime
import speech_recognition as sr
import os
import pyautogui
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=10)

        try:
            print("Recognizing")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except Exception as e:
            speak("Say that again, please")
            return "none"
        return query

def wish():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am jarvis, please tell me how can I help you")

if __name__ == "_main_":
    wish()
    while True:
        query = takecommand().lower()

        if "open notepad" in query:
            path = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(path)
        elif "open cmd" in query:
            path = "C:\\Windows\\System32\\cmd.exe"
            os.startfile(path)
        elif "play video on youtube" in query:
            speak("Which video would you like me to play for you?")
            video_query = takecommand()
            kit.playonyt(video_query)
        elif "power off" in query:
            os.system("shutdown/s/t 1")
        elif "open powerpoint"in query:
            pyautogui.moveTo(740,1036,duration=1)
            pyautogui.click()
            pyautogui.write(' powerpoint',interval=0.25)
            pyautogui.press('enter')
        elif "write something" in query:
            path = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(path)
            speak("what shoud i write sir")
            typequery=takecommand()
            pyautogui.write(typequery)
        
        
        elif "excel"in query:
          pyautogui.moveTo(740,1036,duration=1)
        pyautogui.click()
        pyautogui.write(' excel',interval=0.25)
        pyautogui.press('enter')
