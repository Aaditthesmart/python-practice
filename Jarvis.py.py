import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime 
import webbrowser
import os
import smtplib


engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aaditbansal2008@gmail.com', 'aadit.1234')
    server.sendmail('aaditbansal2008@gmail.com', to, content)
    server.close()  

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good afternoon Sir!")
    
    else:
        speak("Good evening Sir!")

    speak("I am Jarvis ,Please tell me how may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    
    return query 

if __name__=="__main__" :
    wishme()
    while True:
     query=takeCommand().lower()
     
     if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

     elif 'open youtube' in query:
         webbrowser.open("youtube.com")

     elif 'open google' in query:
            webbrowser.open("google.com")

     elif 'open spotify' in query:
            webbrowser.open("spotify.com")
     elif 'open gmail' in query:
            webbrowser.open("gmail.com")

     elif 'open berger paints' in query:
            webbrowser.open("bergerpaints.com")

     elif 'play music' in query:
            music_dir = "C:\\Users\\Dell\\Music\\Bones(PaglaSongs).mp3"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))


     elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        

     elif 'open vscode' in query:
            codePath = "C:\\Users\\Dell\\OneDrive\\Desktop\\Visual Studio Code.lnk"
            os.startfile(codePath)

     elif 'open t launcher' in query:
            gamePath = "C:\\Users\\Public\\Desktop\\TLauncher.lnk"
            os.startfile(gamePath)

     elif 'open chrome' in query:
            chromePath = "C:\\Users\\Public\\Desktop\\Google Chrome.lnk"
            os.startfile(chromePath)

     elif 'email to Aditya' in  query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "aaditbansal2008@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Aadit sir. I am not able to send this email")    