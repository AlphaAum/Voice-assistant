import random
import sys
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import pyaudio
import  wikipedia
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[0].id)
engine.setProperty("voice",voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hours=int(datetime.datetime.now().hour)

    if hours<=12 and hours>4:
        speak("good morning")
        print("good morning")
    elif hours>12 and hours<17:
        speak("good afternoon")
        print("good afternoon")
    else:
        speak("good evening")
        print("good evening")

    speak("hello,i am boot made by om sir.tell me how may i help you?")


def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:


        print("listening.....")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said : {query}")

    except Exception as e:
        print("please speak again")

    return query


if __name__ == '__main__':

    wish()
    while True:
        query=takecommand().lower()


        if "wikipedia" in query:
            speak("serching in wikipedia")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "youtube" in query:
            webbrowser.open("youtube.com")

        elif "google" in query:
            webbrowser.open("google.com")

        elif "w3school" in query:
            webbrowser.open("w3schools.com")

        elif "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif "photo" in query:
            photo_dir= "C:\\Users\\ridpa\\Pictures\\Camera Roll"
            photos=os.listdir(photo_dir)
            a=random.randint(0,len(photos)-1)
            os.startfile(os.path.join(photo_dir,photos[a]))

        elif "play music" in query:
            webbrowser.open("https://www.youtube.com/watch?v=hc7IJO7fD78")

        elif "time" in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"sir the time is {strtime}")

        elif "open vs code" in query:
            codepath= "C:\\Users\\ridpa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "quit" in query:

            sys.exit()

