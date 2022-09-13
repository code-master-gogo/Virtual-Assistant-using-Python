import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib  as smtp 
from email.message import EmailMessage

engine  = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am doughnut. Please tell me how may I help you?")

def takeCommand():
    #It takes microphone input from user and return it's string output.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please!")
        return "None"
    return query

def sendEmail(to_address, content):
    user = 'hyjragynamo@yahoo.com'
    password = 'omvhkyvblqdtdenh'
    fr_address = 'hyjragynamo@yahoo.com'
    smtp_host = 'smtp.mail.yahoo.com' 
    smtp_port = 587
    subject = 'Mail From Virtual Assistant named Doughnut Doggo'
    server = smtp.SMTP(host=smtp_host, port=smtp_port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(user=user, password=password)
    msg = EmailMessage()
    msg['From'] = fr_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.set_payload(content)
    server.send_message(msg)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir = 'D:\\Movies\\Music\\Bhajans'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now(). strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\anubh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to anubhav' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to_address = "anubhavpandey11@gmail.com"
                sendEmail(to_address, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry prabhu dayal! I am unable to send this email!")