import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os 

# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("rate",158)

engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didnt understand")
        return "None"
    return query

if __name__ == '__main__':
    speak(" Namaste Tarun Sir")
    speak("Friday assistance activated ")
    speak("How can i help you  sir")
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)
        elif 'who is the course instructor of this course' in query:
            speak("doctor sd samantaray who is  the head of computer engineering department and his specializations in Artificial Intelligence Natural Language Processing (NLP) Data and Knowledge Mining Cyber Security and Computational Intelligence ")
            print("Dr. S.D. Samantaray who is  the head of computer engineering department and his specializations in Artificial Intelligence, Natural Language Processing (NLP), Data and Knowledge Mining, Cyber Security and Computational Intelligence")
        elif 'who are you' in query:
            speak("I am  friday the voice assistant which are programmed for the course of programming for artificial intelligence and machine learning applications by tarun kumar, mansi bisht, abhinav,deepika verma and yash arya   ")
            print("I am  friday the voice assistant which are programmed for the course of programming for artificial intelligence and machine learning applications by Tarun Kumar, Mansi Bisht, Abhinav,Deepika Verma and Yash Arya ")
        elif 'who is tarun' in query:
            speak("He is an engineering student from pantnagar and he is  my friend ")
            print("He is an engineering student from pantnagar and he is  my friend")
        elif 'who is mansi bisht' in query:
            speak("She is a brilliant engineering student from pantnagar and she is  my friend ")
            print("She is a brilliant engineering student from pantnagar and she is  my friend")
        elif 'who is abhinav' in query:
            speak("He is an engineering student from pantnagar and he is a part of this project ")
            print("He is an engineering student from pantnagar and he is a part of this project")
        elif 'who is deepika' in query:
            speak("she is an tallented engineering student from pantnagar and she is a part of this project ")
            print("she is an tallented engineering student from pantnagar and she is a part of this project")
        elif 'who is yash arya' in query:
            speak("He is an engineering student from pantnagar and he is  my friend ")
            print("He is an engineering student from pantnagar and he is  my friend")
        elif 'give me your contact number' in query:
            speak("9368045239")
            print("9398045239")
        elif 'when is your birthday' in query:
            speak("eighteen january ")
            print("18 january")
        elif 'what is your email id' in query:
            speak("56213_tarunkumar@gbpuat.nic.in")
            print("56213_tarunkumar@gbpuat.nic.in")
        elif 'do you have any facebook account' in query:
            speak("no i dont have any facebook account ")
        elif 'do you have any instagram account' in query:
            speak("yes ")
        elif 'tell me your hobbies' in query:
            speak(" my hobbies are dance, enjoy to some new places and what is your hobbies ")
        elif 'open instagram' in query:
            speak("opening insta id")
            webbrowser.open("https://www.instagram.com")
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com/")
        elif 'open mail' in query:
            speak("opening mail")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        elif 'open location' in query:
            speak("openin location")
            webbrowser.open("https://maps.google.com/")
        elif 'open calendar' in query:
            speak("opening calendar")
            webbrowser.open("https://calendar.google.com/calendar/u/0/r?pli=1")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.open("C://Users\DELL\Desktop\WhatsApp.lnk")
        elif 'play phir miloge na song' in query:
            speak("opening song")
            webbrowser.open("https://youtu.be/n0VNjUNjB-g")
        elif 'open college website' in query:
            speak("opening college website")
            webbrowser.open("http://www.gbpuat-tech.ac.in/")
        elif 'open old registered website' in query:
            speak("opening regi ")
            webbrowser.open("http://gbpuat-regi.com/newregi/default.html")
        elif "temperature" in query:
           search = "temperature in delhi"
           url = f"https://www.google.com/search?q={search}"
           r  = requests.get(url)
           data = BeautifulSoup(r.text,"html.parser")
           temp = data.find("div", class_ = "BNeawe").text
           speak(f"current{search} is {temp}")
        elif "weather" in query:
           search = "temperature in delhi" 
           url = f"https://www.google.com/search?q={search}"
           r  = requests.get(url)
           data = BeautifulSoup(r.text,"html.parser")
           temp = data.find("div", class_ = "BNeaWE").text
           speak(f"current{search} is {temp}")

        elif 'tell me time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)
            print(time)
        elif 'calculate'in query:
            speak("opening calculator")
            webbrowser.open("https://www.google.co.in/search?q=google+calculator&sxsrf=ALiCzsZyByJiPjFUvWJStCjSkBDJ8dA88A%3A1671453940378&ei=9FygY7TXFp7g4-EPnKmqkAw&ved=0ahUKEwi0of-S24X8AhUe8DgGHZyUCsIQ4dUDCA8&uact=5&oq=google+calculator&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIHCAAQsQMQQzIKCAAQgAQQAhDLATIFCAAQgAQyCAgAEIAEELEDMgUIABCABDIFCAAQgAQyCwgAEIAEELEDEIMBMgUIABCABDIFCAAQgAQyCggAEIAEEAIQywE6CggAEEcQ1gQQsAM6BwgAELADEENKBAhBGABKBAhGGABQjA9YqxlgvSFoAXABeACAAZwBiAHbBpIBAzAuNpgBAKABAcgBCsABAQ&sclient=gws-wiz-serp")
        elif 'shut down your system' in query:
            speak("okay thank you  sir")

            exit(0)
