import speech_recognition as sr
import pyttsx3 
import webbrowser
import musiclibrary
from datetime import datetime ,time
import requests
from google import genai
import os



# All the api's
r = sr.Recognizer()
newsapi = "Paste Your News_API Here"
ai_api = "Paste Your Gemini API Here"


# Commands
def processcommand(c):
    c = c.lower()
    if "open google" in c:
        speak("Opening google...")
        webbrowser.open("https://google.com")
        
    elif "open youtube" in c:
        speak("Opening youtube...")
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c:
        speak("Opening linkedin...")
        webbrowser.open("https://linkedin.com")

    elif "open leetcode" in c:
        speak("Opening leetcode...")
        webbrowser.open("https://leetcode.com")
        
    elif c.startswith("play"):
        song = c.split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)  

    else:
        client = genai.Client(api_key=ai_api)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents = c
        )
        print(response.text)
        speak(response.text)


# Converting text to speech    
def speak(text):
    # this function will make the jarvis to speak whatever we want
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)
    engine.say(text)
    engine.runAndWait()
    
now = datetime.now().time()
if __name__ == "__main__":
    speak("Initializing Jarvis.....")

    if time(0,0)<=now<=time(12,0):
        speak("Good Morning Sir.....")
    elif time(12,0)<=now<=time(16,0):
        speak("Good Afternoon Sir.....")
    else: 
        speak("Good Evening sir.....")


while True:
    with sr.Microphone() as source:
        print("Talk")
        word = r.listen(source)
        # recoginze_() method will throw a request
        # error if the API is unreachable,
        # hence using exception handling
        
        try:
            text = r.recognize_google(word)
            print("You said: " + text)
            
            # check if wake word was spoken
            if text.lower() == "jarvis":
                speak("Ya")
                with sr.Microphone() as source:
                    print("Talk")
                    audio_text = r.listen(source)
                    command = r.recognize_google(audio_text)
                    processcommand(command)
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))



        
        
