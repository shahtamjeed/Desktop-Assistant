import pyttsx3
import speech_recognition as sr
import os
import datetime
import webbrowser
import wikipedia
import random



engine=pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Snowbell,How may I help you sir?")

def takeCommand():

        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio=r.listen(source)

        try:
            print("Recogonizing...")
            query= r.recognize_google(audio,language='en-us')
            print(f"User said:{query}\n")
        except Exception as e:
            print(e)
            speak("Say that again please...")
            return "None"
        return query



if __name__ == '__main__':
    speak("Hello")
    wishMe()
    while True:
        query=takeCommand().lower()

        #Logic for AI


        if "wikipedia" in query:
            try:
                speak("Searching Wikipedia...")
                query=query.replace("wikipedia","")
                result=wikipedia.summary(query,sentences=2)
                speak("According to wikipedia.")
                print(result)
                speak(result)
            except:
                speak("No data found in Wikipedia..")

        elif "hello" in query:
            speak("Hello Sir,how are you?")

        elif "youtube" in query:
            speak("Opening Youtube")
            webbrowser.open('www.youtube.com')

        elif "play music" in query:
            speak('Playing Music,Just in seconds.')
            music_dir='E:\\Songs'
            songs=os.listdir(music_dir)
            # songs=[]
            # randomsong = random.randint(0, len(songs))
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "the time" in query:
            srtTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {srtTime}")

        elif "open code" in query:
            try:
                speak("Opening Visual Studio Code...")
                path='C:\\Users\\Tamjeed Shah\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code.exe'
                os.startfile(path)
            except:
                speak("Sorry, can't open V S code,path is not defined.")

        elif "exit" in query:
            speak("Good bye,Happy to help you sir.")
            quit()