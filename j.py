import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        #query = r.recognize_google(audio, language='en-in')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aditirai2611@gmail.com', 'Aditya@2201')
    server.sendmail('aditirai2611@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
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

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            #music_dir = 'D:\\Songs'
            songs = os.listdir('D:\\Songs')
            d=random.choice(songs)
            print(songs)
            #os.startfile(f"D:\\Songs\{d}")  
            os.startfile(os.path.join('D:\\Songs', d))  
            #os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'joke' in query:
            speak('Boy: I am in love with you, totally… Girl: Tu Totla! Tela Baap Totla!')

        elif 'alphabet' in query:
            speak('a b c d e f g h i j k l m n o p q r s t u v w x y z')
        elif 'naam' in query:
            speak('meri pyara dost aditi')
        elif 'english story' in query:
            estory=os.listdir('D:\\Eng story')
            e=random.choice(estory)
            
            os.startfile(os.path.join('D:\\Eng story',e))
            print(estory)

        elif 'hindi story' in query:
            hstory=os.listdir('D:\\Hindi story')
            h=random.choice(hstory)
            print(hstory)
            os.startfile(os.path.join('D:\\Hindi story',h))

        elif 'kannada story' in query:
            kstory=os.listdir('D:\\Kannada story')
            k=random.choice(kstory)
            print(kstory)
            os.startfile(os.path.join('D:\\Kannada story',k))

        elif 'email to aditi' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "aditirai2611@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")
         
        elif 'stop' in query:
            exit()   

        
