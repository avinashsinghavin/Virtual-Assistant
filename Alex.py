import pyttsx3
import wikipedia
import datetime
import webbrowser
import os
from googlesearch import search
import random
import smtplib
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendEmail(to,content):
    server  = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('princeofdeath25@gmail.com','.#Prince1')
    server.sendmail('princeofdeath25@gmail.com',to,content)
    server.close()



def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning! ")
    elif 12 <= hour < 17:
        speak("Good Afternoon")
    else:
        speak("Good Evening ")
    speak("I am Alex Sir, Please say me how may I help You")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold=900
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")
    except Exception as e:
        print(e)
        speak("Say that again please...  ")
        return "None"
    return query

def waitcommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold=900
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")
    except Exception as e:
        print(e)

        return "None"
    return query


if __name__ == "__main__":
    wishme()
    chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s"
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query= query.replace("Wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        if 'open youtube' in query:
            webbrowser.register('chrome', None)
            webbrowser.open('https://www.youtube.com')
        if 'open google' in query:
            query = takeCommand().lower()
            for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
                print(j) 
                webbrowser.register('chrome', None)
                webbrowser.open(j)
            '''
            query=takeCommand().lower()
            #webbrowser.open("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
            webbrowser.register('chrome', None)
            webbrowser.open(query)'''
        
        if 'open stackoverflow' in query:
            webbrowser.register('chrome', None)
            webbrowser.open('https://www.stckoverflow.com')
        if 'close google' in query:
            os.system("taskkill /im chrome.exe /f")
        if 'play music' in query:
            songs = os.listdir('F:\\Fav')
            print(songs)
            x = len(songs)-1
            p = random.randint(0,x)
            os.startfile(os.path.join('F:\\Fav',songs[23]))
        if 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strtime}")
            
        if 'open code' in query:
            path="C:\\Users\\Avinash\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        if 'close code' in query:
            os.system('TASKKILL /F /IM Code.exe')
            
        if 'email to avinash' in query:
            try:
                speak("What should i say")
                content = takeCommand()
                to = "tigeravinash@gmail.com"
                sendEmail(to,content)
                speak("Email Has send")
            except Exception  as e:
                print(e)
                speak(" Sorry sir I am not able to  send this email ")
        
        if 'wait' in query or 'sleep' in query or 'rest' in query:
            while True:
                print('.')
                query=waitcommand().lower()
                if 'start' in query or 'wake up' in query:
                    speak("I am always for your service sir")
                    break
        
        if 'quit' in query or 'exit' in query:
            speak("I hope you liked my service sir, please wake me up when you need me")
            break
            
        if 'your name' in query:
            speak(" My name is Alex")
        if 'hello' in query:
            speak(" hello Sir, how may i help you ")
        if 'open notepad' in query:
            cmd = 'notepad'
            os.system(cmd)
        if 'shutdown' in query:
            os.system('sudo shutdown now')
            
 # speak("Hello Avinash how are you ")
