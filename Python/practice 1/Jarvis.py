# from logging import exception
# from http import server
# from logging import exception

import smtplib
from tkinter import BROWSE
import wikipedia
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os


# list =["browser", "brave","INternet"]
# list = list.lower()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon!")

    else:
        speak("Good Evening")

    speak("I am Jarvis sir! Please tell me how may i help you!")

def takeCommand():
    '''it take microphone input from user and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 400
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recongnizing...")
        query =r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again please..")
    return query

def sendemail(to, content):
    server = smtplib.SMTP('smtplib.gmail.com', 574)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your password')
    server.sendmail('youremail@gamil.com', to , content)
    server.close()

if __name__=='__main__':
    wishMe()
    while True:
        
        query =takeCommand().lower()
    # Logic for executing tasks based on query
        if 'wikipedia'in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia","")
            results =wikipedia.summary(query,sentences=2)
            speak("According to wikilpedia")
            print(results)
            speak(results)
        
        elif'open youtube' in query:
            webbrowser.open('youtube.com')
        elif'open google' in query:
            webbrowser.open('google.com')
        elif'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
        elif'play music' in query:
            # webbrowser.open('stackoverflow.com'
            music_dir='C:\\Users\\hksai\\OneDrive\\Desktop\\Python Course with Notes\\1. Chapter 1'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[-1]))
        elif 'the time' in query:
            strtime =datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir ji, the time is {strtime}")
        elif 'open code' in query:
            codefile = "C:\\Users\\hksai\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codefile)
        elif 'send email to harry' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to ="nameemail@gmail.com"
                sendemail(to, content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my boss, i am not able to send this email")
        elif 'open browser' in query:
            path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(path)
        elif 'your work is done':
            speak('thank for using me sir')
            exit()
        elif 'quit' in query:
            speak('thank for using me sir')
            exit()
        