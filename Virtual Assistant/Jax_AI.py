import pyttsx3
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import random
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning sir..!!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon sir..!!")

    elif hour>=17 and hour<20:
        speak("Good Evening sir..!!")

    else:
        speak("Good Night sir..!!")

    speak("I'm Jax. An AI made by Jax R, how may I help you today..!?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Zaar --> Listening...")
        # r.energy_threshold = 100 
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Zaar --> Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User --> {query}\n")

    except Exception as e:
        print("Zaar --> Say that again please..!!")
        return "None"
    
    return query

if __name__=="__main__":
    greetMe()
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching on Wikipedia..!!")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(f"Zaar --> {results}")
            speak(results)

        elif "youtube open karo" in query:
            webbrowser.open("www.youtube.com")

        elif "google open karo" in query:
            webbrowser.open("www.google.com")

        elif "facebook open karo" in query:
            webbrowser.open("www.facebook.com")

        elif "instagram open karo" in query:
            webbrowser.open("www.instagram.com")

        elif "flipkart open karo" in query:
            webbrowser.open("www.flipkart.in")

        elif "amazon open karo" in query:
            webbrowser.open("www.amazon.in")

        elif "spotify open karo" in query:
            webbrowser.open("www.spotify.com")

        elif "song play karo" in query:
            song_dir = "E:\\Personal\\Sangeet..!!"
            songs = os.listdir(song_dir)
            n = random.randint(0, len(songs) - 1)
            #print(songs)
            os.startfile(os.path.join(song_dir, songs[n]))

        elif "movie play karo" in query:
            movie_dir = "E:\\Personal\\My Movies"
            movies = os.listdir(movie_dir)
            n = random.randint(0, len(movies) - 1)
            # n = random.randint(0, 22)
            #print(movies)
            os.startfile(os.path.join(movie_dir, movies[n]))

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "vs code open karo" in query:
            vs_path = "E:\\Area 51 (Prohibited)\\VS Code\\Microsoft VS Code\\Code.exe"
            os.startfile(vs_path)

        elif "quit" in query:
            speak("Thanks for your time sir..!!")
            exit()


